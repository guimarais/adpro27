"""01.3.E1: validate at the boundary and make rejection reasons observable."""

from pydantic import BaseModel, Field, ValidationError


class Observation(BaseModel):
    label: str = Field(min_length=1)
    value: float = Field(ge=0, allow_inf_nan=False)


rows = [
    {"label": "north", "value": 4},
    {"label": "south", "value": "3.5"},
    {"label": "", "value": 1},
    {"label": "west", "value": -2},
    {"label": "east"},
    {"label": "hill", "value": "broken"},
]
accepted, rejected = [], []
for index, row in enumerate(rows):
    try:
        accepted.append(Observation.model_validate(row))
    except ValidationError as error:
        reasons = [(item["loc"], item["type"]) for item in error.errors()]
        rejected.append((index, reasons))
        print("Rejected", index, reasons)

# Default validation converts the numeric string; it rejects missing fields,
# empty labels, negative quantities, and a string that cannot be a number.
assert len(accepted) == 2 and len(rejected) == 4
assert accepted[1].value == 3.5
print("Accepted:", len(accepted), "Rejected:", len(rejected))
# Expected: rejected indices 2, 3, 4, 5; final counts 2 and 4.
