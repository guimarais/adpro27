"""01.5.H1: validation belongs before collection; preserve failure evidence."""

import json
from pathlib import Path
from pydantic import BaseModel, Field, ValidationError


class Observation(BaseModel):
    label: str = Field(min_length=1)
    value: float = Field(ge=0, allow_inf_nan=False)


class Report:
    def __init__(self, name):
        self.name = name
        self.records = []

    def add(self, observation):
        self.records.append(observation)

    def total(self):
        return sum(record.value for record in self.records)


def build_report(rows):
    report, rejected = Report("validated"), []
    for index, row in enumerate(rows):
        try:
            observation = Observation.model_validate(row)
        except ValidationError as error:
            rejected.append({"index": index, "fields": [item["loc"] for item in error.errors()]})
        else:
            report.add(observation)
    return report, rejected


rows = json.loads(Path("fixtures/observations.json").read_text())
report, rejected = build_report(rows)
assert len(report.records) == 2 and len(rejected) == 4 and report.total() == 6
assert [item["index"] for item in rejected] == [2, 3, 4, 5]
print("Accepted:", len(report.records), "Rejected:", len(rejected), "Total:", report.total())
# Expected: Accepted: 2 Rejected: 4 Total: 6.0
# Catching only ValidationError keeps unrelated programming failures visible.
