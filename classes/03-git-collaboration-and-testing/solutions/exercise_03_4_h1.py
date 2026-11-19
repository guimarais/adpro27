"""Independently runnable reference; pytest also discovers these tests explicitly."""

import pytest
from pydantic import ValidationError

from report_app import source
from report_app.analysis import summarize
from report_app.models import Observation


@pytest.fixture
def observations():
    return [
        Observation(label="north", value=2.5),
        Observation(label="south", value=3.5),
    ]


def test_fixture_total(observations):
    assert summarize(observations)["total"] == 6


@pytest.mark.parametrize("values, expected", [([], None), ([2, 4], 3), ([0], 0)])
def test_mean_cases(values, expected):
    rows = [Observation(label="sample", value=value) for value in values]
    assert summarize(rows)["mean"] == expected


def test_replace_input(monkeypatch):
    monkeypatch.setattr(
        source, "read_payload", lambda: [{"label": "local", "value": 7}]
    )
    assert source.load_observations()[0].value == 7


def test_replacement_still_validates(monkeypatch):
    monkeypatch.setattr(source, "read_payload", lambda: [{"label": "bad", "value": -1}])
    with pytest.raises(ValidationError):
        source.load_observations()


# Run manually from the class root:
# uv run --locked python -m pytest -q solutions/exercise_03_4_h1.py
# The context restores the attribute even when a check raises.
with pytest.MonkeyPatch.context() as patch:
    test_replace_input(patch)
with pytest.MonkeyPatch.context() as patch:
    test_replacement_still_validates(patch)
for values, expected in [([], None), ([2, 4], 3), ([0], 0)]:
    test_mean_cases(values, expected)
print("Parameter cases and isolated input replacements passed.")
