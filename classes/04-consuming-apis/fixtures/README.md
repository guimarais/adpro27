# Saved inputs and provenance

Default lessons and tests use these local inputs. No fixture reads credentials or starts a server.

| File | Source and purpose |
| --- | --- |
| observations.json, north.json | Course-authored quantities, continuing the class-03 north/south example; the latter is the expected exact-label subset |
| invalid-record.json | Course-authored missing-value example, with one valid and one invalid record |
| unavailable.json | Synthetic HTTP 503 body; status is supplied separately by the test helper |
| not-json.html | Synthetic HTTP 200 HTML body demonstrating JSON failure |
| world-bank-population.json | Actual World Bank Indicators API response retrieved on **19 November 2026**, for Spain/Portugal population in 2023; source metadata lastupdated 2026-11-11 |
| openai-response.json, ollama-response.json | **Hand-authored illustrative response subsets**, not live captures or model evaluations; model names are placeholders and must not be used as live model recommendations |
| page-1.json, page-2.json | Synthetic optional pagination example, with three observations across two pages; not the World Bank envelope |

The public response was fetched from [this two-country population request](https://api.worldbank.org/v2/country/PRT;ESP/indicator/SP.POP.TOTL?format=json&date=2023&per_page=2). The saved values are ESP 48,352,528 and PRT 10,578,174 persons. Estimates can be revised; do not assert exact live values in tests. The raw JSON is retained without changing its envelope.

Attribution: **World Bank, World Development Indicators, “Population, total” (SP.POP.TOTL), Spain and Portugal, 2023; retrieved 19 November 2026.** See the [indicator and original-source metadata](https://data.worldbank.org/indicator/SP.POP.TOTL), [data terms](https://data.worldbank.org/summary-terms-of-use), and [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). The World Bank's terms include additional conditions and exceptions indicated in dataset metadata; retain attribution when reusing the data. The lesson's adapter changes representation to ISO/year labels; it does not change the stored values.

The AI subsets follow the [official OpenAI Responses reference](https://developers.openai.com/api/reference/resources/responses/methods/create) and [Ollama generate reference](https://docs.ollama.com/api/generate), checked on 19 November 2026. They omit optional metadata for readability. HTTP-shaped responses constructed by examples/saved_http.py do not prove a real service returned a particular status/body combination.
