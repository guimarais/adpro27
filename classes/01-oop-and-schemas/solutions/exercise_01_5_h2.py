"""01.5.H2: extend the record contract while preserving older input data."""

from pydantic import BaseModel, Field, ValidationError


class UnitObservation(BaseModel):
    label: str = Field(min_length=1)
    value: float = Field(ge=0, allow_inf_nan=False)
    unit: str = Field(default="count", min_length=1)


class MeanReport:
    def __init__(self, name):
        self.name = name
        self.records = []

    def add(self, observation):
        self.records.append(observation)

    def mean(self):
        if not self.records:
            return None
        return sum(record.value for record in self.records) / len(self.records)


filled, empty = MeanReport("filled"), MeanReport("empty")
for row in [{"label": "north", "value": 2.5}, {"label": "south", "value": 3.5}]:
    observation = UnitObservation.model_validate(row)
    assert observation.unit == "count"
    filled.add(observation)
assert filled.mean() == 3 and empty.mean() is None
assert "unit" not in UnitObservation.model_json_schema()["required"]
try:
    UnitObservation(label="north", value=1, unit="")
except ValidationError:
    pass
else:
    raise AssertionError("The unit must be nonempty")
print("Default unit:", filled.records[0].unit, "Means:", filled.mean(), empty.mean())
# Expected: Default unit: count Means: 3.0 None
# The default makes older dictionaries usable; an explicitly invalid unit is
# still rejected. Returning None distinguishes no measurements from mean zero.
