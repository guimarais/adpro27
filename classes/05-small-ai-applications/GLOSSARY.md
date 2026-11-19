# Class 05 glossary

Read the first group before class, then return to the other groups as they appear.
Definitions describe this small application. Examples use the saved 2023 population
data, whose units are persons. This is reference material inside the existing
workload, not an additional reading assignment.

## First encounter — part 05.1

| Term | Meaning | Example here |
| --- | --- | --- |
| Model / LLM | A trained system that generates output from input context; LLM means large language model | OpenAI receives a question and may propose an answer or tool call |
| Prompt | Input asking the model to do something | “What was Portugal's population in the saved 2023 data?” |
| Instructions | Application-provided directions sent with a request | Use permitted tools for numbers; explain missing data |
| Message / role | A piece of conversation content and who supplied it | A `user` message contains the question |
| Token | A unit of text represented by the model; it need not equal a word | The output-token budget limits generation, including reasoning tokens for applicable models |
| Context | The input available for a particular model request | Instructions, the user question, earlier returned items, and tool results |
| SDK | Software development kit: a library for calling a service from code | The `openai` Python package handles HTTP and exposes `client.responses` |
| API key | A secret used to authenticate API access | `OPENAI_API_KEY`, read only after explicit live opt-in |
| Schema | A contract describing accepted data shape and types | `Answer` requires one string field named `answer` |
| Structured output | Model output constrained to an agreed schema | `{"answer": "The snapshot contains two countries."}` |
| Validation | Checking an actual value against a contract | Rejecting `{"answer": 123}`; it does not check factual truth |

## Connecting Python — part 05.2

| Term | Meaning | Example here |
| --- | --- | --- |
| Tool | An application operation offered to the model | The supplied `find_observations(label)` function |
| Tool call / function call | A model's proposal to invoke a named operation with arguments | `find_observations` with `{"label": "PRT:2023"}` |
| Arguments | Named input values passed to a function | `label="PRT:2023"`; `get_summary` takes no arguments |
| Read-only | Able to inspect data without changing it | Returning Portugal's saved observation |
| Allowlist | The complete set of names the application permits | `PERMITTED` contains exactly two entries |
| Dispatcher | Python code that selects and invokes a permitted function | Look up the name, validate arguments, call the function |
| Tool result | Data returned by executing the function | A list containing the Portugal observation |
| Call ID | Identifier connecting a tool proposal with its result | A `function_call_output` returns the same `call_id` |

## Orchestration and evidence — parts 05.3–05.5

| Term | Meaning | Example here |
| --- | --- | --- |
| Harness | Application code around the model: requests, tools, validation, limits, and traces | Supplied `run` coordinates the small explorer |
| Agent | A model-driven application that can choose actions within an application-controlled loop | This bounded, read-only explorer; the name grants no additional permissions |
| Orchestration | Coordinating the steps of an application | Request → validate proposal → execute tool → return result → request answer |
| Stopping condition | A rule that ends a run | A valid final answer, a failure, or an exhausted limit |
| Refusal | A provider response explicitly declining the request | A `refusal` content item; distinguish it from ordinary answer text explaining that writing is unavailable |
| Incomplete response | A response that did not finish | The output-token budget was exhausted; do not parse partial output as success |
| Trace | A record of observable application events | Model request number, proposed tool, actual result, final outcome; not private model reasoning |
| Replay | A fixed saved script replacing model responses | The Portugal script always follows its authored sequence |
| Fixture | A saved input used to make an example or check repeatable | A response proposing an unknown tool |
| Deterministic test | A repeatable check of application behavior using controlled inputs | A third tool proposal never executes |
| Evaluation | Comparing observed behavior with explicit expectations | Checking five prompts for correct numbers, missing-data handling, and read-only behavior |
| Live evidence | Evidence from an actual provider/model request | An explicitly opted-in run, recorded with model/date; mocked SDK transport is not live evidence |

An **API error** means the request failed at the provider boundary, such as a
connection failure or HTTP 429. **Unknown tool**, **invalid arguments**, and
**invalid output** identify different application contract failures. None means
“the population is zero.” See [the failure lesson](05.4-guided-failure-practice.ipynb)
for the named outcomes and manual recovery steps.
