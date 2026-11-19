"""Inspect the request and a saved filtered response without starting a server."""

import requests

from examples.saved_http import saved_response
from report_app.api import LOCAL_URL

# params encodes the query separately from the endpoint; prepare sends nothing.
prepared_request = requests.Request(
    "GET", LOCAL_URL, params={"label": "north"}
).prepare()
response = saved_response("north.json")
response.raise_for_status()
reference_rows = response.json()
assert prepared_request.url.endswith("?label=north")
assert reference_rows == [{"label": "north", "value": 2.5}]
print(prepared_request.method, prepared_request.url, reference_rows[0]["value"])
# Expected: GET ...?label=north and 2.5. This fixture is illustrative HTTP-shaped
# data, not proof a request was sent. Try the manual server/client commands too.
# Browser/docs = frontend; FastAPI = backend; north/south JSON = data source.
