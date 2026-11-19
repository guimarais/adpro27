"""Behavior checks and a corrected mean; no supplied source is overwritten."""


def mean(values):
    """Return the arithmetic mean, or None when there are no values."""
    return sum(values) / len(values) if values else None


def test_two_values_have_the_expected_mean():
    assert mean([2, 4]) == 3


def test_empty_input_has_no_mean():
    assert mean([]) is None


test_two_values_have_the_expected_mean()
test_empty_input_has_no_mean()
assert mean([0]) == 0
# Put this corrected function in a SCRATCH copy of practice/buggy_mean.py.
# From that copy's project root, run: python -m pytest -q practice/test_buggy_mean.py
# The supplied original deliberately fails two tests; the corrected copy passes both.
print("Normal, empty, and zero behavior checked.")
