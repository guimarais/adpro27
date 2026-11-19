"""Run with python -m report_app from the class directory."""

import json
from pathlib import Path

from .models import Observation
from .report import Report


def main() -> None:
    """Read the bundled input, validate it, and print one JSON summary."""
    rows = json.loads(Path(__file__).with_name("sample.json").read_text())
    report = Report("class-02")
    for row in rows:
        report.add(Observation.model_validate(row))
    print(json.dumps({"name": report.name, **report.summary()}, sort_keys=True))


if __name__ == "__main__":
    main()
