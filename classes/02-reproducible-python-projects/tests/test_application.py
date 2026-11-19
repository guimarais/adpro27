"""Instructor checks of boundaries taught in the module/refactoring lessons."""

import json
from pathlib import Path
import subprocess
import sys
import unittest

from report_app.analysis import summarize
from report_app.models import Observation
from report_app.report import Report


class ApplicationChecks(unittest.TestCase):
    def test_state_is_not_shared_between_reports(self):
        left, right = Report("left"), Report("right")
        left.add(Observation(label="north", value=4))
        self.assertEqual(left.summary()["total"], 4)
        self.assertEqual(right.summary(), {"count": 0, "total": 0, "mean": None})

    def test_empty_calculation_has_explicit_contract(self):
        self.assertEqual(summarize([]), {"count": 0, "total": 0, "mean": None})

    def test_module_entry_point_produces_expected_json(self):
        result = subprocess.run(
            [sys.executable, "-m", "report_app"],
            cwd=Path(__file__).resolve().parents[1],
            capture_output=True,
            text=True,
            check=True,
        )
        self.assertEqual(
            json.loads(result.stdout),
            {"name": "class-02", "count": 2, "total": 6, "mean": 3},
        )

    def test_importing_entry_module_does_not_run_the_program(self):
        result = subprocess.run(
            [sys.executable, "-c", "import report_app.__main__; print('imported')"],
            cwd=Path(__file__).resolve().parents[1],
            capture_output=True,
            text=True,
            check=True,
        )
        self.assertEqual(result.stdout.strip(), "imported")


if __name__ == "__main__":
    unittest.main()
