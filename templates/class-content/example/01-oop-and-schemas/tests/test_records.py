"""Behavior checks for the example's state isolation and input boundary."""

import unittest

from pydantic import ValidationError

from examples.records import Observation, Report


class ReportChecks(unittest.TestCase):
    def test_adding_to_one_report_does_not_change_another(self):
        left, right = Report(), Report()
        left.add(Observation(label="north", value=4))
        self.assertEqual(left.total(), 4)
        self.assertEqual(right.total(), 0)
        self.assertEqual(right.records, [])

    def test_invalid_input_is_rejected_before_it_reaches_the_report(self):
        for raw in ({"label": "", "value": 1}, {"label": "west", "value": -2}):
            with self.subTest(raw=raw), self.assertRaises(ValidationError):
                Observation.model_validate(raw)

    def test_default_validation_converts_a_numeric_string(self):
        observation = Observation.model_validate({"label": "south", "value": "3.5"})
        self.assertEqual(observation.value, 3.5)
        self.assertIsInstance(observation.value, float)


if __name__ == "__main__":
    unittest.main()
