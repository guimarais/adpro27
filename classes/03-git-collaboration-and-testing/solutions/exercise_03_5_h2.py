"""Diagnosis and conflict reference; safe to reveal and run in any lesson kernel."""


def mean(values):
    return sum(values) / len(values) if values else None


assert mean([2, 4]) == 3
assert mean([]) is None
assert mean([0]) == 0
resolved_readme = (
    "Quantity report\n"
    "An empty collection has mean None because no measurements exist.\n"
)
assert "<<<<<<<" not in resolved_readme
assert "mean None" in resolved_readme
print(resolved_readme)
# Manual conflict simulation: see 03.5 and INSTRUCTOR.md; use only a scratch repo.
# Resolve README.md according to the agreed contract, then:
# git diff
# git add README.md
# git diff --staged
# git commit -m "Resolve empty-mean contract conflict"
# git status
# Inspect the result AND run behavior checks; removing markers alone is insufficient.
