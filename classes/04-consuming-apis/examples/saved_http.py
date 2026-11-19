"""Supplied fixture setup, so lessons can inspect HTTP without a running server."""

from requests import Response

from report_app.api import LOCAL_URL
from report_app.source import FIXTURES


def saved_response(name: str = "observations.json", status: int = 200) -> Response:
    """Construct an HTTP-shaped teaching response; this is not a network request."""
    response = Response()
    response.status_code = status
    response.url = LOCAL_URL
    response.headers["Content-Type"] = (
        "text/html" if name.endswith(".html") else "application/json"
    )
    response.encoding = "utf-8"
    response._content = (FIXTURES / name).read_bytes()
    return response
