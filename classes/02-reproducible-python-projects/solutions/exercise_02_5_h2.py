"""02.5.H2: handover is a repeatable procedure, not sharing a virtualenv."""

import tomllib
from pathlib import Path

project = tomllib.loads(Path("pyproject.toml").read_text())
assert project["project"]["requires-python"] == ">=3.11"
print("Copy source, input data, pyproject.toml, uv.lock, and README.")
# Do not copy .venv. In the fresh working copy, run these commands manually:
# uv sync --locked
# uv run --locked python -m report_app
# uv run --locked ruff check report_app
# uv run --locked ruff format --check report_app
# Expected: count 2, total 6, mean 3, and passing quality checks.
# Document the class-directory working location and selected notebook kernel.
# The lockfile recreates dependencies; it does not capture every OS component,
# external dataset, or future model answer.
