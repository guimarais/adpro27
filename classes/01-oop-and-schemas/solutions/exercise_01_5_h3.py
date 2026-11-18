"""01.5.H3: checks should distinguish a plausible wrong implementation."""

from pydantic import BaseModel, Field, ValidationError


class Observation(BaseModel):
    label: str = Field(min_length=1)
    value: float = Field(ge=0, allow_inf_nan=False)


class Report:
    def __init__(self):
        self.records = []

    def add(self, observation):
        self.records.append(observation)

    def total(self):
        return sum(item.value for item in self.records)


left, right = Report(), Report()
left.add(Observation(label="north", value=4))
assert len(left.records) == 1 and right.records == []  # catches shared class state
assert right.total() == 0  # catches an incorrect empty-collection contract
try:
    Observation(label="north", value=-1)
except ValidationError:
    pass
else:
    raise AssertionError("Invalid input crossed the boundary")
print("Three behavior checks passed.")
# Design reflection:
# - Report owns accumulated state; a one-off calculation can remain a function.
# - Report contains observations (composition), not a hierarchy of record types.
# - model_dump_json exports instance data; model_json_schema describes a contract.
# - Annotations document intent. Validation enforces the chosen input policy.
