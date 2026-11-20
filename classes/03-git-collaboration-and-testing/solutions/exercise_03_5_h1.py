"""Review reference: independent of earlier answers; no patch is applied here."""

from report_app.analysis import summarize
from report_app.models import Observation

review = {
    "finding": "The patch changes the empty mean from None to zero.",
    "impact": "It makes absent measurements indistinguishable from a measured zero.",
    "request": "Keep None for the empty case and add a regression test.",
    "location": "report_app/analysis.py: empty branch of the mean expression",
}
assert summarize([])["mean"] is None
assert summarize([Observation(label="zero", value=0)])["mean"] == 0
print(review)
# Budget: first 15 minutes for actual PR/peer review or its reserved catch-up,
# then 30 for this regression review. Record the real PR URL/peer comment;
# this reference dictionary and simulated feedback cannot provide that evidence.
# In the prepared scratch COPY: git apply practice/review/change.patch
# Run python -m pytest -q tests/test_reports.py
# Read the failing empty-input assertions. Restore the intended behavior in the copy.
# Do not change the expected result merely to match the faulty patch.
