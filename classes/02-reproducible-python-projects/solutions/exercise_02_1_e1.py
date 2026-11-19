"""02.1.E1: separate a pure calculation from the code calling it."""


def mean_value(values: list[float]) -> float | None:
    """Return the arithmetic mean, or None when no measurements exist."""
    return sum(values) / len(values) if values else None


module_result = mean_value([2, 4])
assert module_result == 3 and mean_value([]) is None
print("Mean:", module_result)
# Expected: Mean: 3.0
# In your scratch project, place the definition in calculations.py.
# In run_report.py use: from calculations import mean_value
# Then call it under if __name__ == "__main__": so imports do not run the app.
# Run python run_report.py from that scratch directory. No sys.path edit needed.
