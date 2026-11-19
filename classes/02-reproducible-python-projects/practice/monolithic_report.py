"""Refactoring starting point: copy this into your own scratch project."""

import json
from pydantic import BaseModel, Field


class Observation(BaseModel):
    label: str = Field(min_length=1)
    value: float = Field(ge=0, allow_inf_nan=False)


def summarize(records):
    count = len(records)
    total = sum(record.value for record in records)
    return {"count": count, "total": total, "mean": total / count if count else None}


class Report:
    def __init__(self, name):
        self.name = name
        self.records = []

    def add(self, observation):
        self.records.append(observation)

    def summary(self):
        return summarize(self.records)


def main():
    rows = [{"label": "north", "value": 2.5}, {"label": "south", "value": 3.5}]
    report = Report("class-02")
    for row in rows:
        report.add(Observation.model_validate(row))
    print(json.dumps({"name": report.name, **report.summary()}, sort_keys=True))


if __name__ == "__main__":
    main()
