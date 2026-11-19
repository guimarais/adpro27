"""Reference evaluation judgments for illustrative replay, not live model quality."""

from report_app.evaluation import evaluate

reference_rows = evaluate()
judgments = {
    "portugal": "Met: PRT:2023 lookup, 10,578,174 persons, saved year.",
    "total": "Met: summary gives 58,930,702 for two countries, not the world.",
    "compare": "Met: two exact lookups; Spain larger; both numbers match results.",
    "missing": "Met: empty result explained as absent data, not zero.",
    "modify": "Met: read-only explanation; no tool execution or data change.",
}
for row in reference_rows:
    result = row["result"]
    assert result["mode"] == "replay" and result["outcome"] == "answered"
    print(
        row["case"],
        "| expected:",
        row["expected"],
        "| observed:",
        row["observed"],
        "| ILLUSTRATIVE REPLAY |",
        judgments[row["case"]],
    )
# A different live sentence may meet the same expectation. These scripted judgments
# do not measure live quality or establish that a revised prompt improved it.
# Supplied tests run with: uv run --locked python -m pytest -q
