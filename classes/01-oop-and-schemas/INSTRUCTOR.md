# Teaching class 01

This is the complete first block, distinct from the short template specimen. Start students at [the index](README.md); the five notebooks are the student-facing reading sequence. The project's domain, milestones, and grading remain separate.

## Class agenda

| Time | Use | Facilitation cue |
| --- | --- | --- |
| 0–20 | 01.1 introduction/demos | Ask students to predict which object changes before running the code |
| 20–30 | 01.1.E1 | Check both values and the explanation of where the list is created |
| 30–50 | 01.2 introduction/demos | Ask what information the calculation needs and why state might justify a class |
| 50–60 | 01.2.E1 | Discuss the empty-report behavior as part of the method's contract |
| 60–80 | 01.3 introduction/demos | Contrast a hint, a converted value, and a rejected value |
| 80–90 | 01.3.E1 | Ask for field/error reasons, not just a count of failed records |

The 15-minute follow-up in each of these parts is independent reading, including the short inheritance/polymorphism example and strict-field comparison. Do not try to teach every follow-up live. Part 01.4 allocates 20 minutes to reading/demos, 15 to its exercise, and ten to review. Part 01.5 allocates 35 + 35 + 20 minutes to its three tasks, with checks/reflection included. Together with setup this matches the index's 90/210-minute allocation; trial the timing with students and shorten work if needed.

## Continuity and deliberate repetition

01.1–01.2 use trusted local dictionaries so the OOP ideas are visible. 01.3 introduces an Observation schema and uses composition to put validated observations in a Report. 01.4–01.5 include that complete baseline. A few short definitions are repeated to make every notebook executable in isolation; they are teaching snapshots, not a proposed application architecture. Week 02 can factor the repeated ideas into modules.

The measurements are explicitly nonnegative quantities. Do not generalize that constraint to temperatures or all data-science measurements. Point out that annotations alone do not check runtime values, that a report does not automatically validate every object passed to it, and that a structural contract does not establish the truth of a measurement.

Inheritance/polymorphism are recognition-level topics here. Prefer the Report-containing-observations example for application design. Keep abstract classes, complex hierarchies, custom validation frameworks, and third-party agent tools outside this block.

## Reference map and expected outcomes

| Exercise | Reference | Observable result |
| --- | --- | --- |
| 01.1.E1 | [exercise_01_1_e1.py](solutions/exercise_01_1_e1.py) | First total 4, second total 0; independent lists |
| 01.2.E1 | [exercise_01_2_e1.py](solutions/exercise_01_2_e1.py) | Mean of 2 and 4 is 3; empty mean is None |
| 01.3.E1 | [exercise_01_3_e1.py](solutions/exercise_01_3_e1.py) | Two accepted records, four rejections with field reasons |
| 01.4.H1 | [exercise_01_4_h1.py](solutions/exercise_01_4_h1.py) | JSON round trip preserves data; schema records required fields and value minimum |
| 01.5.H1 | [exercise_01_5_h1.py](solutions/exercise_01_5_h1.py) | Two accepted, four rejected, total 6; errors retain source index/field |
| 01.5.H2 | [exercise_01_5_h2.py](solutions/exercise_01_5_h2.py) | Default unit works for old inputs, empty unit rejected, mean 3/None |
| 01.5.H3 | [exercise_01_5_h3.py](solutions/exercise_01_5_h3.py) | Checks for state isolation, empty total, and invalid input; design explanation |

Do not reveal a solution by executing its loader as part of teaching setup. Use temporary notebook copies for instructor experimentation; after `%load`, clearing output alone does not restore the distributed loader source.

## Author verification

From this class directory, install authoring tools with `uv sync --locked`. In the complete repository, run the existing shared checker:

```sh
uv run --locked python ../../templates/class-content/verify.py .
```

The checker runs every part in its own fresh kernel, checks the class index/workspace/timing and clean release cells, and runs references independently. It does not claim to automate the VS Code desktop UI. The class folder itself is sufficient for student setup and learning; the shared checker is an instructor repository tool.

For a static preview, from the class directory:

```sh
uv run --locked jupyter nbconvert --to html --output-dir /tmp/adpro-class-01-preview 01.*.ipynb
```

On Windows, choose a temporary output directory and list the five notebook filenames explicitly if the shell does not expand `01.*.ipynb`.

### Verification record

Verified on **18 November 2026** using Linux, Python 3.13.11, Pydantic 2.14.3, ipykernel 7.4.0, IPython 9.18.1, nbformat 5.11.1, nbclient 0.11.0, and nbconvert 7.17.2. Runtime activities use local data and need no GPU or model/API access.

- All five notebooks passed independent fresh-kernel Run All, with blank answer cells and commented references. Execution happened in memory; distributed files retain empty outputs and null counts.
- Ordered filenames/navigation, shared workspace, class-local environment path, all seven full exercise IDs, local links/files, exact loader source, and the 90/210-minute budget passed the shared checker.
- All seven `.py` references ran in separate Python processes with their own setup. Their result assertions and the expected counts/totals in the table above passed.
- Both the existing template and its original short specimen passed regression checks after the checker gained multipart support.
- Original and lesson-prefixed `%load` probes produced replacement payloads without executing the reference; separate execution produced the expected result. These are kernel/protocol checks, **not VS Code GUI checks**.
- Temporary mutation checks rejected a missing ordered lesson, an altered aggregate budget, and overwritten reference-loader source. They did not alter the released class.
- All five notebooks were rendered to static HTML and inspected in the browser. Exercise cards, code, time labels, and required/optional text remained legible without custom styling. The generated previews are review artifacts, not required student dependencies.
- Both `author-class-01-oop-and-schemas` and the updated open template change passed strict OpenSpec validation. Existing and historical teaching materials were preserved.

**Pending desktop check:** the available UI tools do not expose VS Code desktop. On a temporary class copy, select the local `.venv`, restart/run each notebook, inspect the exercise cards, and reveal/execute a reference while preserving a student answer cell. Record the actual editor/extension versions and results when performed. Do not treat the static preview or protocol probe as that GUI result.

The timings are allocations checked for consistency, not measurements from a student trial. Trial them with the cohort and adjust required content within the same budget.

## Illustration update — 19 November 2026

Three local diagrams now support the existing demonstrations; see [sources and teaching notes](IMAGE_SUGGESTIONS.md). Their captions distinguish the analogy from the actual Python behavior. Discuss them within the allocated teaching/reading time. PNG assets retain their source content, with white display backgrounds for transparent diagrams. Creator/license metadata and local image links were checked; the existing pending VS Code desktop verification still applies.

The six updated notebook previews across classes 01 and 02 were rendered and inspected in the browser: all local images loaded, white display backgrounds were applied, and captions/credits were readable. Notebook schema, local links, image paths/dimensions, clean outputs/counts, and exact commented solution loaders passed static checks. No dependency or executable lesson-code changes were needed.


## Course-wide review follow-up — 20 November 2026

**Implementation:** 6 local illustrations now support the existing material.
See [sources, credits, licenses, and editable Mermaid diagrams](IMAGE_SUGGESTIONS.md).
The course-wide changes correct prose/navigation/timing drift while preserving
exercise IDs, answer/loader separation, standalone starts, and the 90/210 budget.

**Difficult-topic cue:** State ownership and the distinction between type hints, coercion, validation, instance JSON, and JSON Schema are the main conceptual risks. Ask students to predict each change/result before running it.

**Automated/static verification:** the template/specimen and all six authored
classes pass the shared fresh-kernel/reference/navigation/release/workload and
`%load` protocol checks, with Requests, HTTPX, and urllib real HTTP blocked.
The existing class-02–06 suites total 100 passing tests; their Ruff lint/format
checks pass. Local image paths, PNG signatures/dimensions, alt text, and embedded
HTML exports pass across all 30 notebooks. No application runtime behavior was
changed by this review.

**Browser verification:** all five class exports load in local headless Chrome
157.0.8103.78 with external HTTP requests blocked. All images load, no page-wide
horizontal overflow was detected, and the actual image cells/captions/credits
and first exercise card of each part were visually inspected in browser
screenshots. The overly tall failure map was compacted and diagrams use their
natural display size. Mermaid CLI 12.2.0 / Mermaid 12.3.0 produced the original
PNGs. Authoring tools/previews live under `/tmp/adpro27-course-visuals`; they are
not new student dependencies. This supersedes earlier local-file-policy limits
for static HTML previews only.

**Still pending:** actual VS Code desktop rendering and reveal/inspect/separately
execute behavior. Browser screenshots and kernel protocol checks do not complete
that task. Beginner timings, supported-platform trials, real hosted PR/deployment/
CI/peer evidence, and live-model checks retain their existing separate status.
Published in `705efd3`, pushed to `origin/main` on **20 November 2026** following the user's explicit commit/push request. No public app deployment or new desktop/live-model/beginner trial is implied.
