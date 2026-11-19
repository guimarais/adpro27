"""Stateful collection, composed from validated observations."""

from .analysis import summarize
from .models import Observation


class Report:
    def __init__(self, name: str):
        self.name = name
        self.records: list[Observation] = []

    def add(self, observation: Observation) -> None:
        """Add an observation already validated at the input boundary."""
        self.records.append(observation)

    def summary(self) -> dict:
        """Compute current results rather than maintain duplicate totals."""
        return summarize(self.records)
