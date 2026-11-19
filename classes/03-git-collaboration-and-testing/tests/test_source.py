"""Replace the input boundary; do not depend on live services or file contents."""

import pytest
from pydantic import ValidationError

from report_app import source


def test_loader_validates_a_replaced_payload(monkeypatch):
    monkeypatch.setattr(
        source, "read_payload", lambda: [{"label": "fixture", "value": 7}]
    )
    records = source.load_observations()
    assert len(records) == 1
    assert records[0].label == "fixture" and records[0].value == 7


def test_loader_rejects_invalid_input(monkeypatch):
    monkeypatch.setattr(
        source, "read_payload", lambda: [{"label": "fixture", "value": -7}]
    )
    with pytest.raises(ValidationError):
        source.load_observations()
