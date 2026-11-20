"""Complete the single dictionary key; all validation/functions are supplied."""

from pydantic import ValidationError
from report_app.tools import FindArguments, dispatch, find_observations

allowed_tools = {"find_observations": find_observations}
name = "find_observations"
validated = FindArguments(label="PRT:2023")
function = allowed_tools[name]  # The missing expression is only name.
reference_records = function(**validated.model_dump())
assert reference_records == [{"label": "PRT:2023", "value": 10578174.0}]
# Change just the validated input; reuse the selected permitted function.
validated = FindArguments(label="FRA:2023")
reference_missing = function(**validated.model_dump())
assert reference_missing == []  # Absent data is not an invented zero.
for bad_name, arguments, expected_error in [
    ("delete_data", "{}", KeyError),
    ("find_observations", '{"label":123}', ValidationError),
]:
    try:
        dispatch(bad_name, arguments)
    except expected_error:
        print(bad_name, "rejected before execution")
    else:
        raise AssertionError("Invalid call unexpectedly accepted.")
print(reference_records)
# Unknown names fail the allowlist. A permitted name can still have invalid args.
