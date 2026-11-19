# Saved data and response provenance

`world-bank-population.json` is copied unchanged from class 04's actual API
snapshot, retrieved **19 November 2026**, source metadata lastupdated 2026-11-11.
It contains Spain 48,352,528 and Portugal 10,578,174 persons for 2023. Estimates
can be revised; this lesson queries the saved snapshot, not current populations.

Attribution: **World Bank, World Development Indicators, “Population, total”
(SP.POP.TOTL), Spain and Portugal, 2023; retrieved 19 November 2026.**
[Original request](https://api.worldbank.org/v2/country/PRT;ESP/indicator/SP.POP.TOTL?format=json&date=2023&per_page=2),
[indicator metadata](https://data.worldbank.org/indicator/SP.POP.TOTL),
[data terms](https://data.worldbank.org/summary-terms-of-use),
[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
Retain attribution and dataset-specific exceptions described by the data terms.
The local adapter changes representation to `ISO:year` labels without changing values.

Every file in `replays/` is a **hand-authored illustrative Responses subset**,
not a live capture or a measurement of a model's quality. The `prompt`, `expected`,
and `steps` fields are course metadata, not provider response fields. Each
`response` shows the relevant provider fields. `expects` checks the actual Python
tool result before returning the next canned response. SDK-only metadata is omitted.

- `structured`: first one-field answer example.
- `portugal`, `total`, `compare`, `missing`, `modify`: five evaluation scripts.
- `unknown-tool`, `invalid-arguments`, `malformed`, `refused`, `incomplete`,
  `repeated`: supplied failure traces; the last proposes a third tool that must not run.

Replay is a fixed script, not a local model. Changing a prompt or its instructions
cannot measure model behavior through replay. To change a scripted scenario,
edit a temporary fixture and its expectations; to test a prompt, opt into live mode.
API errors are raised at the replaced request boundary in tests rather than
invented as successful Responses envelopes. No fixture contains a key or real user input.

The SDK boundary and response shapes follow the [Responses function-calling guide](https://developers.openai.com/api/docs/guides/function-calling)
and [structured-output guide](https://developers.openai.com/api/docs/guides/structured-outputs?api-mode=responses),
checked against official documentation on 19 November 2026. This is documentation
evidence; live compatibility is a separate delivery check.
