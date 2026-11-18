"""01.2.E1: a pure calculation can support an instance method."""


def mean_value(records):
    """Return None when no measurements exist; zero would mean something else."""
    if not records:
        return None
    return sum(record["value"] for record in records) / len(records)


class Report:
    def __init__(self, name):
        self.name = name
        self.records = []

    def add(self, record):
        self.records.append(record)

    def mean(self):
        # The method supplies instance state; the function performs the calculation.
        return mean_value(self.records)


filled, empty = Report("filled"), Report("empty")
filled.add({"label": "north", "value": 2})
filled.add({"label": "south", "value": 4})
assert filled.mean() == 3 and empty.mean() is None
print("Means:", filled.mean(), empty.mean())
# Expected: Means: 3.0 None
# A caller with a list already can use mean_value directly. An instance method
# is convenient when the program already manages a report's state and behavior.
