"""Exercise the real decode/validation path with controlled external responses."""

import pytest
import requests

from examples.ai_http import ollama_response, openai_response
from examples.saved_http import saved_response
from report_app.analysis import summarize
from report_app.api import LOCAL_URL, fetch_observations
from report_app.public_data import parse_population
from report_app.service import observations
from report_app.source import read_fixture


@pytest.fixture
def replace_get(monkeypatch):
    """Replace only acquisition; leave status, JSON, and validation real."""

    def install(response=None, error=None):
        def fake_get(url, *, params, timeout):
            assert url == LOCAL_URL
            assert timeout == 5
            assert params is None or params == {"label": "north"}
            if error is not None:
                raise error
            return response

        monkeypatch.setattr("report_app.api.requests.get", fake_get)

    return install


def test_validated_summary_and_filter(replace_get):
    replace_get(saved_response())
    assert summarize(fetch_observations()) == {"count": 2, "total": 6, "mean": 3}
    replace_get(saved_response("north.json"))
    assert [row.label for row in fetch_observations(label="north")] == ["north"]


@pytest.mark.parametrize(
    "error, message",
    [
        (requests.Timeout(), "timed out"),
        (requests.ConnectionError(), "whether it is running"),
    ],
)
def test_network_failure_is_actionable(replace_get, error, message):
    replace_get(error=error)
    with pytest.raises(RuntimeError, match=message):
        fetch_observations()


@pytest.mark.parametrize("status", [401, 404, 429, 503])
def test_http_status_checked_before_body(replace_get, status):
    replace_get(saved_response("not-json.html", status=status))
    with pytest.raises(RuntimeError, match=f"HTTP {status}"):
        fetch_observations()


def test_invalid_json_is_distinct_from_http_failure(replace_get):
    replace_get(saved_response("not-json.html"))
    with pytest.raises(ValueError, match="invalid JSON"):
        fetch_observations()


def test_one_invalid_record_fails_the_whole_load(replace_get):
    replace_get(saved_response("invalid-record.json"))
    with pytest.raises(ValueError, match="finite, nonnegative"):
        fetch_observations()


def test_supplied_route_function_filters_without_http():
    assert len(observations()) == 2
    assert [row.model_dump() for row in observations(label="north")] == [
        {"label": "north", "value": 2.5}
    ]
    assert observations(label="unknown") == []


def test_public_mapping_keeps_units_and_identity():
    records = parse_population(read_fixture("world-bank-population.json"))
    assert {row.label for row in records} == {"PRT:2023", "ESP:2023"}
    assert all(row.value > 0 for row in records)


def test_missing_population_is_not_silently_zero():
    payload = read_fixture("world-bank-population.json")
    payload[1][0]["value"] = None
    with pytest.raises(ValueError, match="Missing is not zero"):
        parse_population(payload)


def test_partial_public_page_is_not_reported_as_complete():
    payload = read_fixture("world-bank-population.json")
    payload[0]["pages"] = 2
    with pytest.raises(ValueError, match="one complete"):
        parse_population(payload)


def test_ai_replays_need_neither_credentials_nor_network(monkeypatch):
    def forbidden(*args, **kwargs):
        pytest.fail("Replay attempted a live call")

    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    monkeypatch.delenv("OPENAI_MODEL", raising=False)
    monkeypatch.delenv("OLLAMA_MODEL", raising=False)
    monkeypatch.setattr(requests, "post", forbidden)
    assert openai_response()["status"] == "completed"
    assert ollama_response()["done"] is True


def test_explicit_ai_calls_use_documented_http_shapes(monkeypatch):
    calls = []

    def fake_post(url, **kwargs):
        calls.append((url, kwargs))
        return saved_response(
            "openai-response.json" if "openai.com" in url else "ollama-response.json"
        )

    monkeypatch.setenv("OPENAI_API_KEY", "test-key")
    monkeypatch.setenv("OPENAI_MODEL", "selected-test-model")
    monkeypatch.setenv("OLLAMA_MODEL", "installed-test-model")
    monkeypatch.setattr(requests, "post", fake_post)
    openai_response(live=True)
    ollama_response(live=True)
    assert calls[0][0] == "https://api.openai.com/v1/responses"
    assert calls[0][1]["headers"] == {"Authorization": "Bearer test-key"}
    assert calls[0][1]["json"]["model"] == "selected-test-model"
    assert calls[0][1]["timeout"] == 60
    assert calls[1][0] == "http://127.0.0.1:11434/api/generate"
    assert calls[1][1]["json"]["stream"] is False
    assert calls[1][1]["timeout"] == 120
