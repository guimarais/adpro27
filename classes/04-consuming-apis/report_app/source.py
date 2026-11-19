"""Small saved inputs; paths are relative to this module, not the terminal."""

import json
from pathlib import Path

from .models import Observation

FIXTURES = Path(__file__).resolve().parent.parent / "fixtures"


def read_fixture(name: str):
    """Read a named teaching fixture without contacting any service."""
    return json.loads((FIXTURES / name).read_text(encoding="utf-8"))


def load_observations() -> list[Observation]:
    """Preserve the earlier classes' local, validated starting point."""
    return [
        Observation.model_validate(row) for row in read_fixture("observations.json")
    ]
