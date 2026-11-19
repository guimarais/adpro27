"""02.4.H1: improve names and contracts while retaining the calculation."""


def summarize_values(values: list[float]) -> dict:
    """Return count, total, and mean; empty input has total 0 and mean None."""
    count = len(values)
    total = sum(values)
    return {"count": count, "total": total, "mean": total / count if count else None}


assert summarize_values([2, 4]) == {"count": 2, "total": 6, "mean": 3}
assert summarize_values([]) == {"count": 0, "total": 0, "mean": None}
print(summarize_values([2, 4]))
# On a COPY of the exercise file, run manually:
# uv run --locked ruff check path/to/your_file.py
# uv run --locked ruff format path/to/your_file.py
# A minimal README states the required Python version, uv sync --locked,
# the working directory, the run command, expected output, and the check command.
# Formatting does not establish that the mean calculation is correct.
