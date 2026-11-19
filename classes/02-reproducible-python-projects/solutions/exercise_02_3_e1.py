"""02.3.E1: explicit terminal steps; this reference does not install anything."""

import tomllib
from pathlib import Path

manifest = tomllib.loads(Path("pyproject.toml").read_text())
lock = tomllib.loads(Path("uv.lock").read_text())
print("Declared:", manifest["project"]["dependencies"])
print(
    "Resolved Pydantic:",
    next(p["version"] for p in lock["package"] if p["name"] == "pydantic"),
)
# In a NEW scratch location, run manually:
# uv init --bare --vcs none dependency-demo
# cd dependency-demo
# uv add pydantic
# uv run --locked python -c "import pydantic; print(pydantic.__version__)"
# Inspect pyproject.toml and uv.lock, then recreate with uv sync --locked.
# Expected: the manifest declares Pydantic; the lock records exact resolutions.
# uv pip install alone does not perform the same project-metadata operation.
