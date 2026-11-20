"""Reference: diagnose the supplied entrypoint error before inspecting a real build."""

from pathlib import Path
from report_app.source import read_fixture

case = next(
    c for c in read_fixture("deployment-failures.json") if c["id"] == "entrypoint"
)
reference_entrypoint = "streamlit_app.py"
assert Path(reference_entrypoint).is_file()
print(case["log"])
print("Select", reference_entrypoint, "at the student repository root.")
# In Community Cloud, select your own student repo, main, and this entrypoint.
# Select Python 3.13 explicitly. Leave AI secrets empty for required work.
# Expected evidence: next build log and a public URL showing the saved-data app.
# If unavailable, record pending; this invented log is not a real deployment.
