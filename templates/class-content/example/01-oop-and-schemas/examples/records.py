"""Small data contracts and behavior shared by the specimen and its solutions."""

from pydantic import BaseModel, Field


class Observation(BaseModel):
    """One nonnegative measurement with a nonempty label."""

    label: str = Field(min_length=1)
    value: float = Field(ge=0)


class Report:
    """Collect validated observations, with separate state for each report."""

    def __init__(self):
        self.records: list[Observation] = []

    def add(self, record: Observation) -> None:
        """Add an observation already validated at the input boundary."""
        self.records.append(record)

    def total(self) -> float:
        """Return the sum of the stored measurements."""
        return sum(record.value for record in self.records)
