"""A small replaceable input boundary; the default reads only bundled data."""

import json
from pathlib import Path

from .models import Observation


def read_payload() -> list[dict]:
    """Read the two local example records; no live service is contacted."""
    return json.loads(Path(__file__).with_name("sample.json").read_text())


def load_observations() -> list[Observation]:
    """Validate each input record before returning it to the application."""
    return [Observation.model_validate(row) for row in read_payload()]
