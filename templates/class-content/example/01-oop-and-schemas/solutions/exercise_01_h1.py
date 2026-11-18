"""Exercise 01.H1: validate raw records before adding them to a report."""

import json
from pathlib import Path

from pydantic import ValidationError

from examples.records import Observation, Report

# This solution supplies its own input and state; no student answer is required.
raw_records = json.loads(Path("fixtures/observations.json").read_text())
validated_report = Report()
rejected_count = 0

for raw_record in raw_records:
    try:
        observation = Observation.model_validate(raw_record)
    except ValidationError:
        # Invalid labels and negative values are rejected at this boundary.
        rejected_count += 1
    else:
        validated_report.add(observation)

# Default Pydantic validation converts "3.5" to 3.5. It does not mean that
# Python type hints alone enforce values or that all coercion is desirable.
assert len(validated_report.records) == 2
assert rejected_count == 2
assert validated_report.total() == 6
print(f"Accepted: {len(validated_report.records)}; rejected: {rejected_count}")
print(f"Total: {validated_report.total()}")
# Expected result: Accepted: 2; rejected: 2 / Total: 6.0
