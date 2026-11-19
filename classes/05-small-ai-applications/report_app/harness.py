"""Supplied loop: inspect it; students do not implement this module."""

import json

from openai import APIError
from pydantic import ValidationError

from .models import Answer
from .tools import dispatch

MAX_MODEL_REQUESTS = 3
MAX_TOOL_EXECUTIONS = 2


def run(prompt: str, request, *, mode: str = "replay") -> dict:
    """Keep the provider output/history; expose only application events in trace."""
    history = [{"role": "user", "content": prompt}]
    trace = []
    model_requests = 0
    tool_executions = 0

    def finish(outcome, *, answer=None, detail=""):
        trace.append({"event": "finished", "outcome": outcome})
        return {
            "mode": mode,
            "outcome": outcome,
            "answer": answer,
            "model_requests": model_requests,
            "tool_executions": tool_executions,
            "trace": trace,
            "detail": detail,
        }

    while model_requests < MAX_MODEL_REQUESTS:
        model_requests += 1
        trace.append({"event": "model_request", "number": model_requests})
        try:
            response = request(history)
        except APIError as exc:
            # Do not put provider bodies/headers or credentials into a student trace.
            return finish("api_error", detail=type(exc).__name__)
        except ValueError as exc:
            return finish("replay_error", detail=str(exc))
        if not isinstance(response, dict):
            return finish("invalid_response", detail="Expected a Responses object.")
        if response.get("status") == "incomplete":
            return finish(
                "incomplete", detail="Inspect output-token budget and retry manually."
            )
        if response.get("status") != "completed":
            return finish(
                "invalid_response", detail="Expected a completed Responses envelope."
            )
        output = response.get("output", [])
        if not isinstance(output, list) or any(
            not isinstance(item, dict) for item in output
        ):
            return finish("invalid_response", detail="Expected output items.")
        messages = [item for item in output if item.get("type") == "message"]
        if any(
            not isinstance(item.get("content"), list)
            or any(not isinstance(part, dict) for part in item["content"])
            for item in messages
        ):
            return finish("invalid_response", detail="Expected message content items.")
        content = [part for item in messages for part in item["content"]]
        if any(part.get("type") == "refusal" for part in content):
            return finish("refused", detail="The model refused; inspect the request.")
        calls = [item for item in output if item.get("type") == "function_call"]
        texts = [
            part.get("text") for part in content if part.get("type") == "output_text"
        ]
        if calls:
            if len(calls) != 1 or texts:
                return finish(
                    "invalid_response",
                    detail="Expected one tool call and no final text.",
                )
            call = calls[0]
            if not all(
                isinstance(call.get(key), str) and call[key]
                for key in ("name", "arguments", "call_id")
            ):
                return finish(
                    "invalid_response",
                    detail="Tool name, JSON arguments, and call_id are required.",
                )
            trace.append(
                {
                    "event": "tool_proposed",
                    "name": call["name"],
                    "arguments": call["arguments"],
                }
            )
            if tool_executions >= MAX_TOOL_EXECUTIONS:
                return finish(
                    "tool_limit",
                    detail="Two tools executed; this proposed call was not executed.",
                )
            try:
                result = dispatch(call["name"], call["arguments"])
            except KeyError:
                return finish(
                    "unknown_tool", detail="Only the two permitted tool names can run."
                )
            except ValidationError:
                return finish(
                    "invalid_arguments", detail="Check the supplied tool schema."
                )
            tool_executions += 1
            trace.append(
                {"event": "tool_result", "name": call["name"], "result": result}
            )
            # Preserve all output, including provider reasoning items, in history.
            # The public trace contains observable application events, not private reasoning.
            history.extend(output)
            history.append(
                {
                    "type": "function_call_output",
                    "call_id": call["call_id"],
                    "output": json.dumps(result),
                }
            )
            continue
        if len(texts) != 1 or not isinstance(texts[0], str):
            return finish(
                "invalid_output",
                detail="Expected exactly one final answer JSON string.",
            )
        try:
            answer = Answer.model_validate_json(texts[0])
        except ValidationError:
            return finish(
                "invalid_output",
                detail="Expected an object containing only answer: string.",
            )
        return finish("answered", answer=answer.answer)
    return finish("model_limit", detail="No fourth model request was sent.")
