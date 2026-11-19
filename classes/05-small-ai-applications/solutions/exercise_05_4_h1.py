"""Name one failure; a missing country is a different, valid result."""

from report_app.harness import run
from report_app.provider import make_replay
from report_app.source import read_fixture

script = read_fixture("replays/invalid-arguments.json")
reference_failure = run(script["prompt"], make_replay("invalid-arguments"))
expected_outcome = "invalid_arguments"  # Complete only this string.
assert reference_failure["outcome"] == expected_outcome
assert reference_failure["tool_executions"] == 0
# The numeric label 123 violates the argument contract. Keep the schema strict.
for case in ["portugal", "missing"]:
    script = read_fixture(f"replays/{case}.json")
    result = run(script["prompt"], make_replay(case))
    assert result["outcome"] == "answered"
    print("REPLAY:", case, result["answer"])
# A valid string FRA:2023 produces []; its absence is not a population of zero.
# Manual focused command: uv run --locked python -m pytest -q -k saved_failures
print(reference_failure["outcome"])
