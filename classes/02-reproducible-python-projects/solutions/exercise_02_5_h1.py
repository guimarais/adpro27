"""02.5.H1: the provided package is one small refactoring reference."""

from report_app.models import Observation
from report_app.report import Report

reference = Report("class-02")
for row in [{"label": "north", "value": 2.5}, {"label": "south", "value": 3.5}]:
    reference.add(Observation.model_validate(row))
assert reference.summary() == {"count": 2, "total": 6, "mean": 3}
print(reference.summary())
# In your own scratch copy:
# models.py owns Observation; analysis.py owns the pure calculation;
# report.py owns collection state; __main__.py owns reading and printing.
# Use ordinary package imports and an explicit main guard.
# Compare your CLI's parsed JSON with the monolithic starter's result.
# A different small module split is acceptable if the responsibilities are clear.
