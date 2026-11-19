"""Behavior checks: fresh setup, normal/empty data, and invalid inputs."""

import pytest
from pydantic import ValidationError

from report_app.analysis import summarize
from report_app.models import Observation
from report_app.report import Report


@pytest.fixture
def observations():
    """Each requesting test receives new input objects."""
    return [
        Observation(label="north", value=2.5),
        Observation(label="south", value=3.5),
    ]


def test_total_uses_the_records(observations):
    report = Report("daily")
    for observation in observations:
        report.add(observation)
    assert report.summary() == {"count": 2, "total": 6, "mean": 3}


def test_report_instances_have_independent_state(observations):
    left, right = Report("left"), Report("right")
    left.add(observations[0])
    assert left.summary()["count"] == 1
    assert right.summary() == {"count": 0, "total": 0, "mean": None}


@pytest.mark.parametrize("values, expected", [([], None), ([2, 4], 3), ([0], 0)])
def test_mean_contract(values, expected):
    records = [Observation(label="sample", value=value) for value in values]
    assert summarize(records)["mean"] == expected


@pytest.mark.parametrize("value", [-1, "not-a-number"])
def test_invalid_quantity_is_rejected(value):
    with pytest.raises(ValidationError) as error:
        Observation(label="north", value=value)
    assert error.value.errors()[0]["loc"] == ("value",)


def test_float_total_uses_an_appropriate_comparison():
    records = [Observation(label="a", value=0.1), Observation(label="b", value=0.2)]
    assert summarize(records)["total"] == pytest.approx(0.3)
