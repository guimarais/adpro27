"""Write the small client while supplying only its HTTP response offline."""

from unittest.mock import patch

import requests

from examples.saved_http import saved_response
from report_app.analysis import summarize
from report_app.api import LOCAL_URL, parse_observations


def fetch_north():
    response = requests.get(LOCAL_URL, params={"label": "north"}, timeout=5)
    response.raise_for_status()
    return parse_observations(response.json())


with patch("requests.get", return_value=saved_response("north.json")) as get:
    reference_records = fetch_north()
    get.assert_called_once_with(LOCAL_URL, params={"label": "north"}, timeout=5)
assert summarize(reference_records) == {"count": 1, "total": 2.5, "mean": 2.5}
print(summarize(reference_records))
# Expected: one validated record; mean 2.5. Keep HTTP outside Report.__init__.
# parse_observations reuses Pydantic; annotations alone would not check JSON.
