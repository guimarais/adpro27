"""Read the class-04 snapshot locally, preserving its units and validation."""

import json
from pathlib import Path

from .models import Observation

FIXTURES = Path(__file__).resolve().parent.parent / "fixtures"


def read_fixture(name: str):
    return json.loads((FIXTURES / name).read_text(encoding="utf-8"))


def load_observations() -> list[Observation]:
    """The supplied, fixed two-country snapshot is the only data source."""
    metadata, rows = read_fixture("world-bank-population.json")
    if metadata.get("pages") != 1:
        raise ValueError("Expected the complete single-page teaching snapshot.")
    return [
        Observation(label=f"{row['countryiso3code']}:{row['date']}", value=row["value"])
        for row in rows
    ]
