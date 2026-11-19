"""Map public data into the unchanged internal record contract."""

from report_app.analysis import summarize
from report_app.public_data import POPULATION_PARAMS, POPULATION_URL, parse_population
from report_app.source import read_fixture

reference_population = parse_population(read_fixture("world-bank-population.json"))
assert {record.label for record in reference_population} == {"PRT:2023", "ESP:2023"}
assert summarize(reference_population)["count"] == 2
print(POPULATION_URL, POPULATION_PARAMS)
print([record.model_dump() for record in reference_population])

# Reload the fixture so this deliberate change cannot alter the valid result.
invalid_payload = read_fixture("world-bank-population.json")
invalid_payload[1][0]["value"] = None
try:
    parse_population(invalid_payload)
except ValueError as exc:
    assert "Missing is not zero" in str(exc)
    print("Expected rejection:", exc)
else:
    raise AssertionError("Missing population must be rejected, not replaced by zero")

# ISO code + year identifies the observation; value is population in persons.
# The total is only these two countries, not world population. Estimates may
# change with revisions. Missing values must fail; they do not mean zero.
# Explicit live step, from the class directory (manual; not run by this file):
# uv run --locked python -m report_app --public
