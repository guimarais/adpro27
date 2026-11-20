"""Reference: one visible line, with a separate manual UI check."""

from report_app.analysis import summarize
from report_app.source import load_observations

reference_title = "My saved population explorer"
# In streamlit_app.py, change only APP_TITLE to the string above.
# Start the server manually from this folder:
# uv run --locked streamlit run streamlit_app.py --browser.gatherUsageStats=false
# Open the printed local URL and check the changed heading.
# Expected unchanged total: 58,930,702 persons, from two saved 2023 observations.
assert summarize(load_observations())["total"] == 58930702
print(reference_title)
# A Python string/assertion is not evidence that the browser heading was checked.
