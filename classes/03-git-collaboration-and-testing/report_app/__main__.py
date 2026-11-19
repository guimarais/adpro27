"""Run the local example with python -m report_app."""

import json

from .report import Report
from .source import load_observations


def main() -> None:
    report = Report("class-03")
    for observation in load_observations():
        report.add(observation)
    print(json.dumps({"name": report.name, **report.summary()}, sort_keys=True))


if __name__ == "__main__":
    main()
