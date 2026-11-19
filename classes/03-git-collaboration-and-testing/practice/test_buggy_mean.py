"""Intentionally failing target; excluded by the default testpaths setting."""

from practice.buggy_mean import mean


def test_nonempty_mean():
    assert mean([2, 4]) == 3


def test_empty_mean():
    assert mean([]) is None
