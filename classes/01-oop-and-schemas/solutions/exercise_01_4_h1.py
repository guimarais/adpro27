"""01.4.H1: serialized instance data and a schema have different purposes."""

import json
from pydantic import BaseModel, Field, ValidationError


class Observation(BaseModel):
    label: str = Field(min_length=1)
    value: float = Field(ge=0, allow_inf_nan=False)


original = Observation(label="north", value=2.5)
text = original.model_dump_json()
restored = Observation.model_validate_json(text)
schema = Observation.model_json_schema()
assert isinstance(text, str) and json.loads(text) == original.model_dump()
assert restored == original
assert set(schema["required"]) == {"label", "value"}
assert schema["properties"]["value"]["minimum"] == 0
try:
    Observation.model_validate({"label": "north", "value": -1})
except ValidationError:
    pass
else:
    raise AssertionError("A negative quantity must be rejected")
print("Round trip:", restored.model_dump())
print("Required:", schema["required"])
# Expected: label north / value 2.5; required fields label and value.
# The instance contains a measurement. The schema describes permitted structure;
# neither proves that north actually produced 2.5 units.
