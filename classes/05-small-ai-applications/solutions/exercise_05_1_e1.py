"""Read one field; validation checks shape, not truth."""

from pydantic import ValidationError
from report_app.models import Answer
from report_app.provider import structured_demo

parsed = structured_demo()
reference_answer = parsed.answer  # The one missing field name is answer.
assert reference_answer == "A read-only tool returns data without changing it."
try:
    Answer.model_validate_json('{"answer":123}')
except ValidationError:
    print("Expected: numeric answer rejected.")
else:
    raise AssertionError("A numeric answer must fail validation.")
# A string containing a false claim still meets the schema. Check facts separately.
assert Answer(answer="Portugal has zero people.").answer
print("REPLAY:", reference_answer)
