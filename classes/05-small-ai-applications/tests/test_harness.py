"""Behavior at the data, policy, provider, and execution-limit boundaries."""

import copy
import json
from unittest.mock import Mock

import httpx
import pytest
from openai import APIConnectionError, APITimeoutError, OpenAI
from pydantic import ValidationError

from report_app import harness, provider, tools
from report_app.evaluation import EVALUATION_CASES, evaluate
from report_app.models import Answer, Observation
from report_app.source import load_observations, read_fixture
from report_app.tools import dispatch, find_observations, get_summary


def replay(case):
    script = read_fixture(f"replays/{case}.json")
    return harness.run(script["prompt"], provider.make_replay(case))


def test_saved_data_contract_and_exact_lookup():
    assert {r.label: r.value for r in load_observations()} == {
        "PRT:2023": 10578174,
        "ESP:2023": 48352528,
    }
    assert get_summary() == {"count": 2, "total": 58930702, "mean": 29465351}
    assert find_observations("PRT:2023")[0]["value"] == 10578174
    assert find_observations("PRT") == []
    with pytest.raises(ValidationError):
        Observation(label="bad", value=float("inf"))


@pytest.mark.parametrize(
    "arguments",
    [
        "{}",
        '{"label":123}',
        '{"label":""}',
        '{"label":"PRT:2023","extra":true}',
        "not json",
    ],
)
def test_argument_contract_rejects_missing_wrong_extra_and_malformed(arguments):
    with pytest.raises(ValidationError):
        dispatch("find_observations", arguments)


def test_no_argument_tool_rejects_extra_argument():
    with pytest.raises(ValidationError):
        dispatch("get_summary", '{"label":"PRT:2023"}')


@pytest.mark.parametrize(
    "case,outcome",
    [
        ("unknown-tool", "unknown_tool"),
        ("invalid-arguments", "invalid_arguments"),
        ("malformed", "invalid_output"),
        ("refused", "refused"),
        ("incomplete", "incomplete"),
    ],
)
def test_saved_failures_execute_no_tool(case, outcome, monkeypatch):
    spy = Mock(wraps=harness.dispatch)
    monkeypatch.setattr(harness, "dispatch", spy)
    result = replay(case)
    assert result["outcome"] == outcome
    assert result["answer"] is None
    assert result["tool_executions"] == 0
    if case != "invalid-arguments" and case != "unknown-tool":
        spy.assert_not_called()


def test_comparison_uses_two_actual_results_and_stays_within_both_limits():
    result = replay("compare")
    assert result["outcome"] == "answered"
    assert result["model_requests"] == 3
    assert result["tool_executions"] == 2
    values = [
        e["result"][0]["value"] for e in result["trace"] if e["event"] == "tool_result"
    ]
    assert values == [10578174, 48352528]
    assert "Spain" in result["answer"]


def test_third_tool_is_proposed_but_never_executed(monkeypatch):
    spy = Mock(wraps=harness.dispatch)
    monkeypatch.setattr(harness, "dispatch", spy)
    result = replay("repeated")
    assert result["tool_executions"] == spy.call_count == 2
    assert result["outcome"] == "tool_limit"
    assert result["model_requests"] == 3


def test_model_limit_is_checked_before_next_request(monkeypatch):
    monkeypatch.setattr(harness, "MAX_MODEL_REQUESTS", 1)
    request = Mock(wraps=provider.make_replay("portugal"))
    result = harness.run("A supplied lookup", request)
    assert result["outcome"] == "model_limit"
    assert result["model_requests"] == request.call_count == 1


def test_replay_checks_tool_output_instead_of_masking_a_broken_dispatch(monkeypatch):
    monkeypatch.setattr(harness, "dispatch", lambda *args: [])
    assert replay("portugal")["outcome"] == "replay_error"


def test_schema_acceptance_does_not_establish_factual_truth():
    assert Answer(answer="Portugal has zero people.").answer
    with pytest.raises(ValidationError):
        Answer.model_validate({"answer": 123})


def test_five_prompt_table_is_replay_evidence_and_missing_is_not_zero():
    rows = evaluate()
    assert tuple(row["case"] for row in rows) == EVALUATION_CASES
    assert all(row["result"]["mode"] == "replay" for row in rows)
    assert all(row["result"]["outcome"] == "answered" for row in rows)
    assert rows[3]["result"]["tool_executions"] == 1
    assert "absent" in rows[3]["observed"]
    assert rows[4]["result"]["tool_executions"] == 0


def test_default_replay_does_not_construct_a_client_or_read_environment(monkeypatch):
    def forbidden(*args, **kwargs):
        raise AssertionError("Default replay must not read live configuration.")

    monkeypatch.setattr(provider, "OpenAI", forbidden)
    monkeypatch.setattr(provider.os, "getenv", forbidden)
    monkeypatch.setattr(type(provider.os.environ), "get", forbidden)
    assert provider.structured_demo().answer
    assert replay("portugal")["outcome"] == "answered"


@pytest.mark.parametrize("error", [APIConnectionError, APITimeoutError])
def test_api_error_stops_with_a_safe_detail(error):
    request = Mock(
        side_effect=error(request=httpx.Request("POST", "https://example.invalid"))
    )
    result = harness.run("A prompt", request, mode="live")
    assert result["mode"] == "live"
    assert result["outcome"] == "api_error"
    assert result["detail"] == error.__name__
    assert request.call_count == 1


def sdk_response(payload):
    """Add SDK metadata omitted from the human-readable teaching subsets."""
    result = copy.deepcopy(payload)
    result.update(id="resp_test", created_at=0, object="response", model="test-model")
    for index, item in enumerate(result["output"]):
        item["id"] = f"item_{index}"
        item["status"] = "completed"
        if item["type"] == "message":
            item["role"] = "assistant"
            for content in item["content"]:
                if content["type"] == "output_text":
                    content["annotations"] = []
    return result


def install_sdk_transport(monkeypatch, handler):
    """Use the installed SDK and its HTTP codec, replacing only real transport."""
    clients = []

    def client_factory(**kwargs):
        client = OpenAI(
            api_key="test-only-placeholder",
            http_client=httpx.Client(transport=httpx.MockTransport(handler)),
            **kwargs,
        )
        clients.append(client)
        return client

    monkeypatch.setenv("OPENAI_MODEL", "test-model")
    monkeypatch.setenv("OPENAI_API_KEY", "test-only-placeholder")
    monkeypatch.setattr(provider, "OpenAI", client_factory)
    return clients


def test_live_request_uses_real_sdk_codec_and_preserves_tool_history(monkeypatch):
    script = read_fixture("replays/portugal.json")
    requests = []

    def handler(request):
        requests.append(json.loads(request.content))
        payload = sdk_response(script["steps"][len(requests) - 1]["response"])
        return httpx.Response(200, json=payload)

    clients = install_sdk_transport(monkeypatch, handler)
    try:
        result = harness.run(
            script["prompt"], provider.make_live_request(), mode="live"
        )
        assert result["outcome"] == "answered"
        assert (
            result["mode"] == "live"
        )  # Transport replacement is still not a live-model check.
        assert len(requests) == 2
        first, second = requests
        assert first["parallel_tool_calls"] is False
        assert first["text"]["format"]["schema"]["required"] == ["answer"]
        assert first["max_output_tokens"] == 1024
        assert {tool["name"] for tool in first["tools"]} == {
            "get_summary",
            "find_observations",
        }
        assert second["input"][-1]["call_id"] == "call_1"
        assert json.loads(second["input"][-1]["output"])[0]["value"] == 10578174
    finally:
        for client in clients:
            client.close()


def test_sdk_status_error_has_no_hidden_retry(monkeypatch):
    attempts = []

    def handler(request):
        attempts.append(request)
        return httpx.Response(
            429,
            json={
                "error": {"message": "Synthetic rate limit", "type": "rate_limit_error"}
            },
        )

    clients = install_sdk_transport(monkeypatch, handler)
    try:
        result = harness.run("A prompt", provider.make_live_request(), mode="live")
        assert result["outcome"] == "api_error"
        assert result["detail"] == "RateLimitError"
        assert len(attempts) == 1
        assert clients[0].timeout == 20.0
    finally:
        for client in clients:
            client.close()


def test_standalone_parse_demo_with_installed_sdk(monkeypatch):
    payload = sdk_response(
        read_fixture("replays/structured.json")["steps"][0]["response"]
    )
    clients = install_sdk_transport(
        monkeypatch, lambda request: httpx.Response(200, json=payload)
    )
    try:
        assert (
            provider.structured_demo(live=True).answer
            == "A read-only tool returns data without changing it."
        )
    finally:
        for client in clients:
            client.close()


def test_parallel_proposal_is_rejected_before_dispatch(monkeypatch):
    response = read_fixture("replays/portugal.json")["steps"][0]["response"]
    response["output"] *= 2
    spy = Mock()
    monkeypatch.setattr(harness, "dispatch", spy)
    result = harness.run("A prompt", lambda history: response)
    assert result["outcome"] == "invalid_response"
    spy.assert_not_called()


@pytest.mark.parametrize("case", ["unknown-tool", "invalid-arguments"])
def test_invalid_proposals_never_reach_the_permitted_function(case, monkeypatch):
    function = Mock()
    monkeypatch.setitem(
        tools.PERMITTED, "find_observations", (tools.FindArguments, function)
    )
    assert replay(case)["tool_executions"] == 0
    function.assert_not_called()


@pytest.mark.parametrize(
    "response",
    [
        None,
        {"status": "failed", "output": []},
        {"status": "completed", "output": ["not an output item"]},
        {"status": "completed", "output": [{"type": "message", "content": None}]},
    ],
)
def test_invalid_response_envelopes_stop_without_executing(response):
    result = harness.run("A prompt", lambda history: response)
    assert result["outcome"] == "invalid_response"
    assert result["tool_executions"] == 0


def test_reasoning_item_is_preserved_in_history_but_not_displayed():
    script = read_fixture("replays/portugal.json")
    first = copy.deepcopy(script["steps"][0]["response"])
    reasoning = {
        "type": "reasoning",
        "id": "rs_test",
        "summary": [],
        "encrypted_content": "synthetic-test-item",
    }
    first["output"].insert(0, reasoning)
    histories = []

    def request(history):
        histories.append(copy.deepcopy(history))
        return first if len(histories) == 1 else script["steps"][1]["response"]

    result = harness.run(script["prompt"], request)
    assert result["outcome"] == "answered"
    assert reasoning in histories[1]
    assert "synthetic-test-item" not in json.dumps(result["trace"])
