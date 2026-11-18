# Advanced Programming for Data Science: course redesign

Agreed curriculum, 18 November 2026. This document is the blueprint for authoring the teaching materials; the existing notebooks have not yet been rewritten.

## Purpose and audience

Students enter with basic Python programming knowledge. They should leave able to build, debug, test, and hand over a small data application that another person can run and maintain. The course develops software engineering habits around data work, external APIs, and small AI applications.

Do not assume previous experience with Git, terminals, virtual environments, HTTP, testing, SQL, cloud services, or LLM APIs. Introduce the relevant concepts when needed. No GPU is required.

The course project is designed and assessed separately by the instructor. The classroom example and exercises support the same general skills but do not specify the project, its domain, milestones, rubric, or grading.

## Agreed constraints

| Item | Design |
| --- | --- |
| Duration | Six weeks, with one main topic per week |
| Required teaching workload | Five hours per week: 90 minutes in class and 210 minutes of independent work |
| Total teaching workload | 30 hours: nine contact hours and 21 independent hours |
| Project workload | Additional to the five weekly hours; managed separately by the instructor |
| Extensions | Clearly optional; allow up to three additional hours of enrichment per week, separate from project work |
| Class rhythm | Three cycles of approximately 20 minutes of teaching/demo and 10 minutes of exercise |
| Classroom coverage | Introduce the initial portion of each block live; develop and consolidate the rest through guided independent work |
| Required foundations | Applied OOP, schemas, virtual environments, pip, uv, and Git |
| AI | Students may use coding assistants throughout, while explaining, testing, and modifying their work; dedicated AI teaching concerns building an application |
| Main AI provider | OpenAI, using direct SDK calls |
| Local AI alternative | Optional Ollama, tested on CPU-only hardware before recommending a model |
| Access | Required exercises remain completable without purchasing model credits |
| Deployment | A small Streamlit application published from GitHub through Streamlit Community Cloud |
| Optional deployment topic | Podman for container packaging and local execution |

Five hours is a budget for required activity, including reading, setup, account preparation, troubleshooting, and completion checks. Move extra work into extensions rather than silently adding it to this budget. Because the project is additional, the course does not promise a five-hour total student workload.

## Learning outcomes

By the end of the course, students should be able to:

1. Choose between functions and small classes; use explicit state and composition, and recognize simple inheritance.
2. Define data contracts using type hints and Pydantic, validate incoming data, and relate a Python model to JSON Schema.
3. Organize Python modules, manage an isolated environment, declare dependencies, and recreate a project using uv and its lockfile.
4. Use Git to inspect changes, make meaningful commits, work on a branch, and collaborate through a pull request.
5. Write readable code and focused documentation; test normal and failure behavior using pytest and fixtures.
6. Consume an HTTP API using parameters, JSON, authentication concepts, pagination, explicit timeouts, and controlled failure handling.
7. Build a small AI harness with permitted tools, validated arguments and results, execution limits, and a small evaluation set.
8. Publish a usable data application with configuration, safe credential handling, useful logs, and automated checks.

Successful completion means demonstrating these behaviors, not recalling a list of commands or library names.

## Six-block sequence

| Week | Main topic | Main classroom artifact |
| --- | --- | --- |
| 1 | OOP and schemas | A small class and validated data records |
| 2 | Reproducible, maintainable Python projects | A structured, runnable project with declared dependencies |
| 3 | Git, collaboration, and testing | A reviewed change with meaningful tests |
| 4 | Consuming APIs | An API client that returns validated records and handles failures |
| 5 | Small AI applications | A bounded tool-calling application with tested orchestration |
| 6 | Deployment and automated delivery | A public application URL and automated repository checks |

Git instruction starts at the beginning of week 3. Weeks 1 and 2 use downloaded starter folders and supplied run instructions. Students do not need to understand cloning, commits, or branches to complete those weeks.

## Teaching approach and classroom example

Use one evolving **public-data explorer**, separate from the assessed project. It loads a small collection of records, validates them, produces a deterministic summary, acquires live data through an API, adds a small AI interface, and finally exposes a thin web UI.

The authoring default is a domain-neutral record with an identifier, category, and numeric measurement. Select a suitable public dataset and key-free teaching API when preparing week 4, then document the mapping into that record. Keep domain analysis simple: the objective is programming rather than statistical modeling. Use saved responses to teach pagination or failures when the live API does not naturally provide them.

Progress the example in small steps:

| Week | Example increment |
| --- | --- |
| 1 | Validate records and use a small collection/report class; keep calculations as functions where appropriate |
| 2 | Move the code into modules; add environment metadata, run instructions, and basic quality checks |
| 3 | Track the example with Git; propose a behavior change through a branch and test it |
| 4 | Replace a saved input with an HTTP client while preserving the validated internal record format |
| 5 | Let a model request one or two read-only operations on the validated data |
| 6 | Publish the data explorer; make AI an optional feature enabled through server-side configuration |

Supply a working starter and a reference solution for every week. A student can start the current week without finishing the previous week's exercises. Before Git is taught, distribute ZIP downloads. From week 3, include cloning and branch-based distribution instructions.

Keep business logic in Python modules. Notebooks remain useful for explanations, exploration, and short demonstrations. Avoid network calls or model downloads in class constructors: construction should establish a usable object; explicit methods perform external operations.

Every exercise should have a small observable result, a hint, and an answer explanation. A broken environment or absent API key should have a documented recovery path rather than becoming the exercise itself.

Assign the setup and account-preparation portions before the relevant class, using that week's independent-work allowance. This includes week 1's initial run check, week 3's GitHub authentication, and week 6's hosting account preparation; none is uncounted prerequisite work.

## Week 1: OOP and schemas

**Question:** How do we represent data and behavior without letting invalid input spread through a program?

**Outcomes:** Create and use instances; distinguish instance state from shared state; organize related behavior; explain composition and one simple inheritance example; validate a record and interpret a validation error.

### Ninety-minute class

| Time | Activity |
| --- | --- |
| 0–20 | Model one record collection: objects, attributes, methods, and construction |
| 20–30 | Exercise: create two instances, change one, and explain why the other should remain unchanged |
| 30–50 | Separate calculations from state; use composition; recognize inheritance through a small example |
| 50–60 | Exercise: add a summary operation and explain whether it belongs in a function or a method |
| 60–80 | Introduce type hints, Pydantic fields, constraints, and validation errors |
| 80–90 | Exercise: validate a dictionary and identify which malformed records should be rejected |

### Independent work: 210 minutes

| Minutes | Work |
| --- | --- |
| 30 | Complete the supplied setup check; run the starter using copyable instructions |
| 45 | Guided reading on object state, composition, type hints, and schemas |
| 90 | Extend the class and data model; validate missing, out-of-range, and incorrectly typed values |
| 45 | Inspect serialization and generated JSON Schema; explain two design choices and correct an invalid input |

**Completion evidence:** A working class, a validated record, an invalid-record example, and a short explanation of why the class is useful.

**Depth limit:** One plain class and one Pydantic model are enough. Briefly show inheritance and polymorphism; defer deep hierarchies, abstract base classes, metaclasses, and design-pattern catalogs. Explain that type hints alone do not validate runtime data, and that default validation may coerce values. Show a deliberate strict-field example without turning strictness into a separate topic. Connect JSON Schema to external contracts rather than teaching its complete specification. [Pydantic models](https://docs.pydantic.dev/latest/concepts/models/), [JSON Schema](https://docs.pydantic.dev/latest/concepts/json_schema/).

**Extension:** Add a nested schema or compare two reasonable object designs.

## Week 2: Reproducible, maintainable Python projects

**Question:** How does a script become a project that someone else can understand and run?

**Outcomes:** Split code into modules, use normal imports, identify the active environment, distinguish pip installation from uv project management, explain the roles of `pyproject.toml` and `uv.lock`, and improve readability and run instructions.

### Ninety-minute class

| Time | Activity |
| --- | --- |
| 0–20 | Organize the week 1 code into modules with a clear entry point |
| 20–30 | Exercise: move a function, fix the import, and run the example |
| 30–50 | Explain virtual environments and a minimal `python -m venv` / `python -m pip` workflow; introduce uv |
| 50–60 | Exercise: identify the interpreter and verify where a dependency is installed |
| 60–80 | Use the supplied uv project: declared dependencies, lockfile, environment recreation, and run commands |
| 80–90 | Exercise: add a dependency through uv, inspect the metadata change, and reproduce the run |

### Independent work: 210 minutes

| Minutes | Work |
| --- | --- |
| 30 | Read the project layout and a concise naming/docstring guide |
| 75 | Refactor the example into modules; improve naming, small functions, type hints, and useful docstrings |
| 60 | Recreate the environment in a fresh working copy; compare declared dependencies with resolved versions |
| 45 | Run formatting/lint checks and write a short README that a peer can follow |

**Completion evidence:** A runnable project, dependency metadata and lockfile, readable modules, and independently followed run instructions.

**Depth limit:** Use uv as the normal course workflow after explaining venv and pip. Distinguish `uv add` from pip-style installation; avoid maintaining two competing dependency specifications. The uv workflow manages the project environment and resolved dependencies. A dependency lockfile does not freeze external API data or model answers. [uv projects](https://docs.astral.sh/uv/guides/projects/), [pip compatibility](https://docs.astral.sh/uv/pip/compatibility/).

Use Ruff for introductory formatting and lint feedback, with a small supplied configuration. Do not make students configure a stack of overlapping tools. [Ruff](https://docs.astral.sh/ruff/).

The starter should not require Git operations in this block. If the installed uv version initializes a repository automatically, leave it unexplained until week 3; do not let generated scaffolding change the teaching sequence. Publishing packages, build backends, and advanced static type checking are extensions.

**Extension:** Add a small command-line argument or explore package publication conceptually.

## Week 3: Git, collaboration, and testing

**Question:** How do we change a shared program while retaining evidence of what changed and whether it works?

**Outcomes:** Inspect a working tree and diff, stage and commit a coherent change, use a branch and pull request, review a peer's change, and write tests that distinguish correct from incorrect behavior.

### Ninety-minute class

| Time | Activity |
| --- | --- |
| 0–20 | Start with Git basics: repository, working tree, staging, commits, status, diff, and history |
| 20–30 | Exercise: inspect a change, stage the intended files, and make a meaningful commit |
| 30–50 | Branch, merge, remote, push/pull, and a simple GitHub pull-request workflow |
| 50–60 | Exercise: publish a small branch and open or review a pull request using a supplied guide |
| 60–80 | Introduce pytest: observable behavior, assertions, and normal/failure cases |
| 80–90 | Exercise: write a test that fails for an actual bug, then verify the correction |

### Independent work: 210 minutes

| Minutes | Work |
| --- | --- |
| 60 | Practice inspecting history and diffs, committing, and working on a branch; complete account/authentication setup if needed |
| 45 | Pair asynchronously: review a small pull request and incorporate feedback |
| 75 | Add normal and failure tests; use fixtures and a small parametrized example |
| 30 | Diagnose a failing test and explain a small merge conflict using supplied examples |

**Completion evidence:** A short Git history, a reviewed pull request, and tests that detect a deliberately introduced error.

**Depth limit:** Teach `.gitignore`, distinguish Git from GitHub, and track source and lockfiles rather than environments or credentials. Use a separate starter working directory for the Git exercises. Prioritize everyday collaboration over Git graph theory. Explain that `pull` fetches and integrates changes; it does not simply replace local code. Show safe recovery of a committed change with a prepared `revert` example. Do not make destructive reset commands part of the beginner recovery workflow.

Tests should check behavior rather than reproduce implementation details. Use standard imports rather than modifying `sys.path` in each test. Introduce replacement of external calls through a supplied fixture/helper and reuse that idea in weeks 4 and 5. [pytest fixtures](https://docs.pytest.org/en/stable/how-to/fixtures.html), [replacing external calls](https://docs.pytest.org/en/stable/how-to/monkeypatch.html).

**Extension:** Resolve a small conflict hands-on or add a regression test to a second pull request.

## Week 4: Consuming APIs

**Question:** How do we acquire useful data when a remote service can fail or return unexpected content?

**Outcomes:** Explain a request/response exchange, send query parameters, check status, parse JSON, map it to an internal schema, and handle network and data failures without hiding them.

### Ninety-minute class

| Time | Activity |
| --- | --- |
| 0–20 | Explain HTTP at the client level; inspect a small GET request and JSON response |
| 20–30 | Exercise: change a parameter and extract a useful field |
| 30–50 | Write a small client function with an explicit timeout, status handling, and schema validation |
| 50–60 | Exercise: diagnose a saved response with a missing field or unexpected status |
| 60–80 | Introduce pagination, authentication headers, rate limits, and bounded retries of suitable read-only requests |
| 80–90 | Exercise: complete a supplied two-page response traversal or classify failures as retryable/non-retryable |

### Independent work: 210 minutes

| Minutes | Work |
| --- | --- |
| 45 | Read the chosen API's documentation and a short HTTP failure guide |
| 60 | Integrate a live endpoint with the example's internal schema |
| 75 | Use fixtures to handle a timeout, HTTP error, invalid JSON/record, and a pagination boundary |
| 30 | Explain the authentication/configuration example and demonstrate an actionable error message |

**Completion evidence:** Validated records from an API, an explicit timeout, and deterministic tests of at least two failure behaviors.

**Depth limit:** Use one synchronous HTTP client, Requests, for the required HTTP exercises. Requests documents parameters, status checking, exceptions, and explicit timeouts. Reuse a supplied bounded-retry helper instead of requiring a general retry framework. Teach authentication with a mock/example if the live teaching API is key-free. Do not require async programming, OAuth implementation, or API server development. [Requests quickstart](https://requests.readthedocs.io/en/latest/user/quickstart/).

**Extension:** Build a small API endpoint, add a cache, or explore asynchronous requests.

## Week 5: Small AI applications

**Question:** How do we make a model useful inside a program whose behavior we can still inspect and check?

**Outcomes:** Make a model request or replay a saved response; define tool contracts; dispatch only permitted functions; validate arguments and final output; enforce a stopping condition; distinguish application tests from model evaluation.

The **harness** is the application's code around the model: request context, available tools, validation, tool execution, response handling, limits, and evidence about results. Teach that code explicitly.

### Ninety-minute class

| Time | Activity |
| --- | --- |
| 0–20 | Make a direct OpenAI SDK request and parse a structured result using a schema |
| 20–30 | Exercise: inspect the result and handle a supplied malformed, incomplete, or refused response |
| 30–50 | Offer one or two read-only Python tools; inspect the proposed call, validate arguments, execute it, and return its result |
| 50–60 | Exercise: complete a supplied dispatcher and reject an unknown tool or invalid argument |
| 60–80 | Add the bounded loop, observable outcomes, and a small evaluation set; compare deterministic checks with live model quality |
| 80–90 | Exercise: diagnose a saved tool-call trace and add a test for the call limit |

### Independent work: 210 minutes

| Minutes | Work |
| --- | --- |
| 30 | Configure available OpenAI access or the replay path; read the optional local Ollama instructions |
| 60 | Extend the supplied harness with a permitted data query or summary operation |
| 60 | Test saved successful and failing tool calls, invalid output, and stopping conditions |
| 45 | Evaluate five supplied prompts against explicit expected behavior; use live access when available and replay traces otherwise |
| 15 | Explain one failure and whether the fix belongs in the schema, tool, prompt, or application logic |

**Completion evidence:** An inspected execution trace, schema validation, bounded execution, deterministic orchestration tests, and a small table of expected versus observed results. Label replay results separately from live model results.

**Main path:** Use direct OpenAI SDK calls. Function calling connects the model to application functions; structured outputs describe the response contract. Python structured-output examples can use Pydantic models. Handle refusal, incomplete output, and API errors explicitly; a valid schema does not establish factual correctness. [OpenAI function calling](https://developers.openai.com/api/docs/guides/function-calling), [structured outputs](https://developers.openai.com/api/docs/guides/structured-outputs).

**No-payment path:** Supply recorded model responses and a small replay client behind the same model-call boundary. Required implementation and tests must work without a paid key. Include a live instructor demonstration or its recording. Offer institution-funded access if available; do not assume it exists. A replay demonstrates orchestration and debugging, not the student's live model performance.

**Optional Ollama path:** Supply separate setup instructions for the Ollama application/server, downloaded model, and Python dependency. Select a small model only after testing tool calling and structured output on representative CPU-only hardware. Verify their combination rather than assuming every model supports it; separate the tool-calling stage from the structured final-answer stage if necessary. Keep provider-specific calls visible and small. [Ollama Python prerequisites](https://github.com/ollama/ollama-python), [tool calling](https://docs.ollama.com/capabilities/tool-calling), [structured outputs](https://docs.ollama.com/capabilities/structured-outputs).

**Depth limit:** One model, one or two read-only tools, and a supplied small call limit. Do not execute arbitrary code proposed by the model. Treat retrieved text as data, not authority to change the tool policy. Inspect the returned numbers against the deterministic tools. Do not require a framework, a universal provider abstraction, RAG, vector databases, or multi-agent orchestration.

**Extension:** Run the same evaluation locally with Ollama, compare a prompt revision, or explore RAG using existing optional material. Local model installation/download time counts toward the extension budget.

## Week 6: Deployment and automated delivery

**Question:** How does a working local program become an application another person can use?

**Outcomes:** Run a supplied thin Streamlit UI, deploy it from GitHub, configure it without committing credentials, read a useful log, and inspect automated test/format checks after a change.

### Ninety-minute class

| Time | Activity |
| --- | --- |
| 0–20 | Wrap the existing data functions in a supplied Streamlit interface; explain configuration and public behavior |
| 20–30 | Exercise: run the UI locally with saved data and make a visible change |
| 30–50 | Connect the repository to Streamlit Community Cloud; inspect dependency installation and deployment logs |
| 50–60 | Exercise: publish the app or diagnose a supplied deployment failure while a build completes |
| 60–80 | Inspect a supplied GitHub Actions workflow, useful logs, and server-side configuration |
| 80–90 | Exercise: push a small tested change, inspect the check result, and verify the deployed version |

### Independent work: 210 minutes

| Minutes | Work |
| --- | --- |
| 45 | Prepare the hosting account, GitHub connection, and deployment checklist |
| 60 | Complete the deployment and fix a supplied or encountered configuration/dependency issue |
| 60 | Adapt the minimal workflow to run tests and formatting/lint checks on pushes and pull requests |
| 30 | Improve logs and missing-configuration behavior; document local and hosted run instructions |
| 15 | Ask a peer to open the public URL and follow the README; record the result |

**Completion evidence:** A public URL that works without AI credentials, a readable README, useful diagnostic output, and a passing automated check for a subsequent change.

**Hosting path:** Streamlit Community Cloud provides GitHub-connected hosting. Its dependency detection recognizes `uv.lock`; keep the uv manifest and lockfile together and avoid introducing a competing deployment requirements file. Use the same selected Python version locally and in hosting. [Community Cloud](https://docs.streamlit.io/deploy/streamlit-community-cloud), [dependency handling](https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/app-dependencies).

**AI deployment boundary:** The required online data application must remain useful with AI disabled. Students with suitable OpenAI access may enable an AI feature using server-side secrets and a small request limit. Never publish an instructor's unrestricted key in the sample or require public anonymous model usage. A remote app's `localhost` refers to that remote machine, so it does not connect to the student's laptop Ollama by default. [Streamlit runtime](https://docs.streamlit.io/deploy/streamlit-community-cloud/status#linux-environments), [secrets management](https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/secrets-management).

**Automation scope:** Use one supplied GitHub Actions job to install the environment and run offline tests plus formatting/lint checks. Include no live model/API calls or model downloads in required CI. Start from the documented uv integration rather than teaching workflow YAML from scratch. Hosting updates and CI checks are separate mechanisms; do not imply that auto-deployment automatically waits for a passing workflow. [uv GitHub Actions integration](https://docs.astral.sh/uv/guides/integration/github/), [GitHub Actions concepts](https://docs.github.com/en/actions/get-started/understand-github-actions).

Explain that GitHub Pages serves static sites; it is not the runtime for this Python app. GitHub supplies the repository and automation, while Streamlit supplies application hosting. [GitHub Pages](https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages).

**Optional Podman extension:** Build an image from a short supplied Containerfile, run it, publish its port locally, and explain what the image packages. Distinguish this from publishing a public service. Podman installation uses a virtual machine on macOS/Windows, so prepare platform-specific instructions. Keep container-to-host Ollama networking outside the required exercise. [Podman installation](https://podman.io/docs/installation), [building images](https://docs.podman.io/en/latest/markdown/podman-build.1.html), [running containers](https://docs.podman.io/en/latest/markdown/podman-run.1.html).

## Completion checks and responsible AI use

Use the weekly completion evidence for short formative checks and feedback. A student should be able to explain their code, make a small change without blindly regenerating it, and show why their checks would catch a plausible error. Coding-assistant use is permitted; verification remains the student's responsibility.

These checks are teaching activities, not a new project rubric or a decision about assessment weights. The existing introduction records quizzes, a group project, and an exam, including historically stated university constraints. Align future quiz/exam questions with the new learning outcomes when those materials are authored; the instructor owns assessment policy and the separate project.

Use a small end-of-course handover exercise on the classroom example: a peer follows the README, runs the checks, and opens the deployed app. Account for this inside week 6 rather than adding an extra assignment.

## Existing materials: reuse and replacement map

Paths below refer to materials present in this repository. Reuse concepts and examples after review; copying an existing notebook wholesale is not the migration strategy.

| Existing material | Destination | Authoring action |
| --- | --- | --- |
| [Course introduction](Notebooks/00-Introduction.ipynb) | Course overview | Rewrite outcomes, sequence, workload, and AI/deployment expectations; confirm assessment-policy text separately |
| [Setup](Notebooks/00.1-SettingUp.ipynb), [software versions](Notebooks/00.2-Software_Versions.ipynb) | Minimal week 1 setup and week 2 | Replace the conda-first route with brief venv/pip foundations and the uv project workflow; retain conda as optional reference |
| [OOP introduction](Notebooks/01-ObjectOrientedProgramming.ipynb), [objects demo](Notebooks/01.1-ObjectOrientedProgramming2.ipynb), [examples](Notebooks/01.2-MoreExamples.ipynb) | Week 1 | Retain small object examples; shorten historical material and emphasize explicit state, composition, and function/class choices |
| [Pydantic](Notebooks/02.4-Pydantic.ipynb), [example 1](Functions/pydantic_example1.py), [example 2](Functions/pydantic_example2.py) | Week 1, revisited in 4–5 | Extend dictionary validation into boundary contracts, serialization, JSON Schema, and error interpretation; remove redundant model constructor boilerplate |
| [Style guide](Notebooks/01.3-StyleGuide.ipynb), [documentation](Notebooks/02-DocumentationAndTesting.ipynb), [docstrings](Notebooks/02.1-FirstSteps.ipynb), [linting examples](Linting/) | Week 2 | Retain naming/docstring exercises; replace tool accumulation with a small Ruff configuration; move full Sphinx generation to optional material |
| [Variable types](Notebooks/02.2-EnforcingVariableTypes.ipynb) | Weeks 1–2 | Clearly distinguish annotations, runtime validation, and static checking; make full mypy instruction optional |
| [Error handling](Notebooks/02.3-ErrorHandling.ipynb), [handled function](Functions/my_function_handled.py) | Weeks 3–5 | Teach failures through tests, network boundaries, and invalid model output; prioritize actionable errors over broad exception swallowing |
| [Version control](Notebooks/03-VersionControl.ipynb), [Git demo](git_demo/GitDemo.md) | Start of week 3 | Modernize the hands-on GitHub workflow; shorten theory, correct pull/recovery explanations, and replace hard-reset-centered beginner recovery |
| [pytest](Notebooks/02.5-TestingWithPytest.ipynb), [test examples](Tests/test_my_first_function.py) | Week 3, reused in 4–6 | Add fixtures and behavior-focused failures; use normal imports; separate deliberately failing numerical examples from the working reference suite |
| [File download](Examples/00-DownloadingAFile.ipynb), [download script](Examples/filedownload.py), [online reader](Functions/online_file_reader.py) | Week 4 | Reuse request/file-boundary ideas; add dedicated HTTP, status, pagination, timeout, authentication, schema, and fixture coverage |
| [Python and LLMs](Notebooks/04.1-Python+LLM.ipynb), [agents](Notebooks/04.2-Agents.ipynb) | Week 5 | Replace framework-first examples with visible direct SDK calls, schemas, a small tool dispatcher, bounded execution, and explicit evaluation |
| [Local Ollama](Notebooks/04.3-Local_LLMs_with_Ollama.ipynb) | Week 5 extension | Update setup and verify the chosen model on CPU-only hardware; separate server/model installation from the Python client |
| [Local RAG](Notebooks/04.3.1-RAG_ollama.ipynb), [OpenAI RAG](Notebooks/04.4-RAG_openai.ipynb), [smart dataframes](Notebooks/04.5-LLMs_Data_Analytics_SmartDataframes.ipynb) | Optional AI material | Retain for enrichment after checking current dependencies; remove from the required learning path |
| `Notebooks/05*.ipynb` time-series sequence | Optional data-analysis material | Retain as reference/enrichment; remove the required time-series block |
| `Notebooks/06*.ipynb` scalability/Dask sequence | Optional scalable-computing material | Retain as reference/enrichment; remove distributed computing from required outcomes |
| [Filesystem appendix](Notebooks/Appendix_1-Filesystem_Navigation.ipynb) | Just-in-time support | Supply short terminal/path reminders alongside setup and module exercises |
| [Past projects](Past_Editions/) | Instructor reference | Preserve as historical material; the instructor designs the new course project independently |
| Deployment and CI | New week 6 material | Author a thin Streamlit example, hosting guide, server-side configuration notes, minimal workflow, and optional Podman guide |

## Teaching materials to author next

For each week, prepare a short concept notebook or reading, a 90-minute instructor agenda, three small class exercises, guided independent work totaling 210 minutes, a starter, and an explained reference solution. Mark optional extensions explicitly.

The sample application can grow toward the following modest structure. Introduce files only when their purpose is taught; this is an authoring sketch, not an additional week 1 requirement.

```text
classroom-example/
  README.md
  pyproject.toml
  uv.lock
  data_app/
    __init__.py
    __main__.py
    models.py
    analysis.py
    api.py
    ai.py
  streamlit_app.py
  tests/
    fixtures/
  .github/
    workflows/
```

Keep reusable logic in the modules and the UI thin. Keep recorded API/model responses small enough to inspect. Provide default saved-data and replay modes, with explicit switches to live services. No plugin architecture or provider framework is required.

Before releasing the revised teaching materials:

1. Run the week 1 setup on supported student operating systems, and count its time in the week 1 budget.
2. Choose the public dataset/API, verify its classroom availability and usage conditions, and save representative responses, including failure/pagination fixtures.
3. Select a supported Python version and dependency set; recreate the environment on a fresh machine and verify the hosting runtime matches.
4. Choose an OpenAI model supporting the taught tools and structured outputs; confirm current account access and costs before offering live student access. Do not hard-code a model choice into the syllabus.
5. Test the replay path without an API key or Ollama. Test any recommended Ollama model separately on representative CPU-only hardware.
6. Verify the chosen Streamlit dependency route, GitHub authentication steps, offline CI, and a complete deployment without AI credentials.
7. Trial the three ten-minute class exercises and the 210-minute independent tasks with a beginner; shorten required work if they overrun.
8. Update navigation and assessment-topic references to match the six blocks. Preserve historical notebooks and project briefs as reference material.

These are implementation checks for the forthcoming materials. This blueprint does not claim that those materials or infrastructure have already been built.

## Technical references

Primary documentation was checked during planning on 18 November 2026. The links next to each technical decision identify its source. Recheck installation instructions, SDK examples, model support, hosting availability, and account requirements when authoring and before teaching; keep course examples pinned and tested for that delivery.
