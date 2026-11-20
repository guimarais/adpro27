"""Reference: useful diagnostic output without private exception contents."""

from report_app.source import read_fixture

reference_log = "data_load_failed kind=ValueError"
print(reference_log)
case = next(
    c for c in read_fixture("deployment-failures.json") if c["id"] == "dependency"
)
print("For the dependency case:", case["small_fix"])
# The data_load_failed event points instead to the local fixture/schema boundary.
# Restore the supplied fixtures, rerun tests, and inspect the next app run.
# Do not log str(exc), keys, passcodes, request headers, or full provider responses.
# Expected evidence: stage/cause, one small fix, safe diagnostic, and actual rerun outcome.
# Missing AI configuration must still leave the saved-data app/replay usable.
