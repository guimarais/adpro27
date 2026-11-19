"""A proposed third tool must never execute; complete one number."""

from report_app.harness import run
from report_app.provider import make_replay
from report_app.source import read_fixture

script = read_fixture("replays/repeated.json")
reference_run = run(script["prompt"], make_replay("repeated"))
assert reference_run["outcome"] == "tool_limit"
assert reference_run["tool_executions"] == 2  # The one missing literal is 2.
assert reference_run["model_requests"] == 3
proposals = [e for e in reference_run["trace"] if e["event"] == "tool_proposed"]
results = [e for e in reference_run["trace"] if e["event"] == "tool_result"]
assert len(proposals) == 3 and len(results) == 2
print("REPLAY: third proposal blocked; two tools, three requests.")
# The third proposal has no result; the unchanged supplied tests also spy on calls.
