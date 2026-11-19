"""Calculations over validated records, with no input/output side effects."""

from .models import Observation


def summarize(records: list[Observation]) -> dict:
    """Return count, total, and mean; an empty collection has mean None."""
    count = len(records)
    total = sum(record.value for record in records)
    return {"count": count, "total": total, "mean": total / count if count else None}
