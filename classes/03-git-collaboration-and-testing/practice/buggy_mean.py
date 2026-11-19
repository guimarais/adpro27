"""Intentionally wrong input for the testing exercise; work on a copy."""


def mean(values):
    return sum(values) / (len(values) + 1) if values else 0
