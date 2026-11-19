"""Produce evidence for human evaluation, without pretending to grade prose."""

from .harness import run
from .provider import make_live_request, make_replay
from .source import read_fixture

EVALUATION_CASES = ("portugal", "total", "compare", "missing", "modify")


def evaluate(*, live: bool = False) -> list[dict]:
    request = make_live_request() if live else None
    rows = []
    for case in EVALUATION_CASES:
        script = read_fixture(f"replays/{case}.json")
        result = run(
            script["prompt"],
            request if live else make_replay(case),
            mode="live" if live else "replay",
        )
        rows.append(
            {
                "case": case,
                "expected": script["expected"],
                "observed": result["answer"] or result["outcome"],
                "result": result,
            }
        )
    return rows
