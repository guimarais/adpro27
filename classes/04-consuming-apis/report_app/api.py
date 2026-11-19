"""A synchronous GET boundary: request, check, decode, validate."""

import requests
from pydantic import TypeAdapter, ValidationError

from .models import Observation

LOCAL_URL = "http://127.0.0.1:8000/observations"


def get_json(url: str, params: dict | None = None):
    """Fetch JSON with a timeout; explain which boundary failed."""
    try:
        response = requests.get(url, params=params, timeout=5)
        response.raise_for_status()
    except requests.Timeout as exc:
        raise RuntimeError(
            "Request timed out; check the service and try again later."
        ) from exc
    except requests.HTTPError as exc:
        status = exc.response.status_code
        raise RuntimeError(
            f"HTTP {status}; check the endpoint, parameters, and access."
        ) from exc
    except requests.RequestException as exc:
        raise RuntimeError(
            "Cannot reach the API; check its address and whether it is running."
        ) from exc
    try:
        return response.json()
    except requests.exceptions.JSONDecodeError as exc:
        raise ValueError(
            "The API returned invalid JSON; inspect its response body."
        ) from exc


def parse_observations(payload) -> list[Observation]:
    """Reject the complete result if any record is invalid; never silently skip."""
    try:
        return TypeAdapter(list[Observation]).validate_python(payload)
    except ValidationError as exc:
        raise ValueError(
            "Expected a list of records with a nonempty label and a finite, nonnegative value."
        ) from exc


def fetch_observations(
    url: str = LOCAL_URL, label: str | None = None
) -> list[Observation]:
    """Keep HTTP acquisition separate from the Report and summary calculation."""
    params = {"label": label} if label is not None else None
    return parse_observations(get_json(url, params=params))
