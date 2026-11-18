"""01.1.E1: __init__ creates a separate list for every report instance."""


class Report:
    def __init__(self, name):
        self.name = name
        self.records = []

    def add(self, record):
        self.records.append(record)

    def total(self):
        return sum(record["value"] for record in self.records)


left, right = Report("left"), Report("right")
left.add({"label": "north", "value": 4})
# Each instance owns a fresh list. We are adding to one list, not a class list.
assert left.records is not right.records
assert (left.total(), right.total()) == (4, 0)
print("Totals:", left.total(), right.total())
# Expected: Totals: 4 0
