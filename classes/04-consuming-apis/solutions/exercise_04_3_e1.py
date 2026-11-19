"""Classify status, JSON and record failures without swallowing them."""

from unittest.mock import patch

from examples.saved_http import saved_response
from report_app.api import fetch_observations

reference_failures = []
for name, status, message in [
    ("unavailable.json", 503, "HTTP 503"),
    ("not-json.html", 200, "invalid JSON"),
    ("invalid-record.json", 200, "finite, nonnegative"),
]:
    with patch(
        "report_app.api.requests.get", return_value=saved_response(name, status)
    ):
        try:
            fetch_observations()
        except (RuntimeError, ValueError) as exc:
            assert message in str(exc)
            reference_failures.append(str(exc))
        else:
            raise AssertionError("The invalid result should have failed")
assert len(reference_failures) == 3
print(*reference_failures, sep="\n")
# Expected: three distinct failures. Never return [] on error: [] means a valid
# successful response with no matches, and would hide why acquisition failed.
