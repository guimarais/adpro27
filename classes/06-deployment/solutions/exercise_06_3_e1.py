"""Reference: one release edit followed by distinct manual CI/hosting checks."""

from pathlib import Path

reference_release = "06.1"
assert "python -m pytest" in Path(".github/workflows/checks.yml").read_text()
# Change RELEASE = "06.0" to RELEASE = "06.1" in streamlit_app.py.
# Run the supplied tests, lint, and format commands locally, then manually:
# git diff -- streamlit_app.py
# git add streamlit_app.py
# git diff --cached
# git commit -m "Show release 06.1"
# git push
# git rev-parse HEAD
# Open Actions for that commit and record the run URL/result.
# Independently open the public app and verify Release 06.1.
# A passed CI job does not itself prove hosting updated; a push is not a build result.
print(
    "Target release:",
    reference_release,
    "— record actual CI and URL evidence separately.",
)
