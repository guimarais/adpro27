"""Reference: adapt a supplied workflow command without removing checks."""

from pathlib import Path

original = "uv run --locked python -m pytest -q"
reference_command = "uv run --locked python -m pytest tests -q --maxfail=1"
workflow = Path(".github/workflows/checks.yml").read_text()
# This reference inspects text only; it does not write YAML or run terminal commands.
assert original in workflow or reference_command in workflow
print(reference_command)
# Replace only the Tests step's run value with reference_command.
# It still discovers all tests; --maxfail=1 stops after the first failure.
# Run the command manually, followed by the supplied Ruff commands.
# Review/stage the workflow, commit/push, and inspect its exact Actions run.
# Expected evidence: the adapted command in a passing hosted job; pending if unavailable.
