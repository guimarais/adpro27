"""Exercise 01.1: each constructor call creates a fresh list of records."""

from examples.records import Observation, Report

left_reference = Report()
right_reference = Report()
left_reference.add(Observation(label="north", value=4))

# Storing the list on self inside __init__ keeps it separate for each instance.
# Adding to the left report therefore does not change the right report.
reference_totals = (left_reference.total(), right_reference.total())
assert reference_totals == (4, 0)
print(f"Left: {reference_totals[0]}; right: {reference_totals[1]}")
# Expected result: Left: 4.0; right: 0
