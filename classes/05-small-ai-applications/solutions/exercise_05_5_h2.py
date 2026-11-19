"""A short explained failure analysis; no additional implementation task."""

from report_app.harness import run
from report_app.provider import make_replay
from report_app.source import read_fixture

script = read_fixture("replays/repeated.json")
reference_reflection = run(script["prompt"], make_replay("repeated"))
assert reference_reflection["outcome"] == "tool_limit"
# Observed: a third summary is proposed; Python executes only the first two.
# Responsible layer: application logic enforces the cap correctly. No loop fix is
# needed for this saved scenario. Prompt/context changes might reduce repetition,
# but replay cannot establish their effect on a model; test that live separately.
# If a third execution actually happened, repair the pre-execution guard and run
# the supplied dispatch-spy regression test, not just a prompt experiment.
# Evidence limit: this trace is illustrative replay, not a live-model evaluation.
print("REPLAY: application limit held; inspect repetition separately.")
