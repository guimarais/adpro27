"""Two focused behavior tests; also executable as an independent reference."""

from unittest.mock import patch

import pytest
import requests

from examples.saved_http import saved_response
from report_app.api import fetch_observations


def test_timeout_reports_the_problem():
    with patch("report_app.api.requests.get", side_effect=requests.Timeout()):
        with pytest.raises(RuntimeError, match="timed out"):
            fetch_observations()


def test_invalid_record_is_rejected():
    with patch(
        "report_app.api.requests.get",
        return_value=saved_response("invalid-record.json"),
    ):
        with pytest.raises(ValueError, match="finite, nonnegative"):
            fetch_observations()


# We replace acquisition, not validation. If timeout handling or validation is
# removed, these checks fail rather than merely reproduce implementation steps.
if __name__ == "__main__":
    test_timeout_reports_the_problem()
    test_invalid_record_is_rejected()
    reference_checks = "timeout and invalid record rejected"
    print(reference_checks)
