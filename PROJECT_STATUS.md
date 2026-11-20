# Course redesign execution status

Updated **20 November 2026**. This page tracks delivery of the [agreed curriculum](COURSE_REDESIGN.md); each linked OpenSpec checklist retains the detailed tasks. Implementation, verification, and publication are separate states.

## Published baseline

- `aaaf0f7`: curriculum redesign and content-template specification.
- `11dc49e`: VS Code teaching template/specimen and complete class 01.
- `04bd438`: complete classes 02–03, illustrations for classes 01–02, class-03 image suggestions, and related specifications/shared verification updates. Pushed to `origin/main` on 19 November 2026.
- `a08a152`: class 04 API lessons, reviewed examples, course execution/authoring records, and explicit pending-image work. Pushed to `origin/main` on 19 November 2026. Image download/embedding/visual review was outstanding at that published baseline; the local 20 November follow-up below completes task 4.5.
- `568bcaa`: complete class 05 lessons, progressive glossary, supplied bounded AI application/replay, and verification/specification records. Pushed to `origin/main` on 19 November 2026. Browser/desktop and live-model delivery checks remain pending.

- `705efd3`: complete class 06, the six-class consistency review, 24 additional CC/Mermaid visuals, browser-preview evidence, and updated specifications/verification guidance. Pushed to `origin/main` on **20 November 2026**. Desktop, hosted student delivery, live-model, and beginner/platform checks remain separate.

These commits identify the published course-material baseline. Publication records describe successful pushes; pending implementation and visual/editor checks retain their separate status.

## Delivery by block

| Area | Implemented and checked | Still outstanding |
| --- | --- | --- |
| [Template and specimen](templates/class-content/AUTHORING.md) | VS Code workspace/setup, notebook/Python/Markdown conventions, exercise cards, commented `%load`, fresh-kernel and static checks; [tasks](openspec/changes/add-course-content-template/tasks.md) | Desktop reveal interaction and visual checks: tasks 5.4–5.5 |
| [01 — OOP and schemas](classes/01-oop-and-schemas/README.md) | Five ordered notebooks, seven references, schemas/serialization, six local CC/CC0 illustrations (three original Mermaid diagrams); automated/protocol/static checks recorded in [instructor notes](classes/01-oop-and-schemas/INSTRUCTOR.md); [tasks](openspec/changes/author-class-01-oop-and-schemas/tasks.md) | Actual VS Code desktop check: task 5.6 |
| [02 — Reproducible Python projects](classes/02-reproducible-python-projects/README.md) | Five ordered notebooks, six references, complete local package, pip/venv/uv practice, four application checks, Ruff, fresh-copy recreation, six local CC illustrations (three original Mermaid diagrams); [instructor notes](classes/02-reproducible-python-projects/INSTRUCTOR.md); [tasks](openspec/changes/author-class-02-reproducible-python-projects/tasks.md) | Actual VS Code desktop check: task 3.6 |
| [03 — Git, collaboration, and testing](classes/03-git-collaboration-and-testing/README.md) | Five ordered notebooks, six references, passing default suite (10 tests), separately targeted reference (6 tests), seeded-bug/patch correction checks, isolated Git workflows, four local CC/Mermaid illustrations plus the source guide; [instructor notes](classes/03-git-collaboration-and-testing/INSTRUCTOR.md); [tasks](openspec/changes/author-class-03-git-collaboration-and-testing/tasks.md) | Actual VS Code desktop check: task 3.6; author checks did not exercise a hosted GitHub PR/authentication flow |
| [04 — Consuming APIs](classes/04-consuming-apis/README.md) | Five ordered notebooks, six references, supplied FastAPI service, minimal Requests client, World Bank mapping/snapshot, illustrative OpenAI/Ollama previews; 15 default tests + 2 reference checks, fresh kernels with HTTP blocked, real localhost/public smoke tests, fresh-copy recreation, Ruff and strict OpenSpec; [content review and two corrections](classes/04-consuming-apis/REVIEW.md), [four local CC/Mermaid illustrations](classes/04-consuming-apis/IMAGE_SUGGESTIONS.md), and offline browser preview review (tasks 4.5/3.4); [instructor record](classes/04-consuming-apis/INSTRUCTOR.md), [tasks](openspec/changes/author-class-04-consuming-apis/tasks.md) | Actual VS Code desktop interaction: task 3.6; live AI/model and cross-platform delivery checks remain separate |
| [05 — Small AI applications](classes/05-small-ai-applications/README.md) | Five ordered notebooks, six references, progressive glossary, two supplied read-only tools, validated bounded harness, direct OpenAI SDK/replay, five-prompt evaluation; 32 tests, fresh kernels with HTTP blocked, mocked SDK codec, seeded regression, fresh-copy recreation, Ruff, five local Mermaid illustrations, offline browser preview review (task 3.7), strict OpenSpec; [instructor record](classes/05-small-ai-applications/INSTRUCTOR.md), [tasks](openspec/changes/author-class-05-small-ai-applications/tasks.md) | Actual VS Code desktop: task 3.6; live instructor/model, optional CPU Ollama, and platform/timing checks pending; original baseline published in `568bcaa`, follow-up published in `705efd3` |
| [06 — Deployment and automated delivery](classes/06-deployment/README.md) | Five ordered notebooks, six references, supplied Streamlit app and class-05 harness, root-layout student hosting/Actions, safe optional AI, diagnostics and Podman guide; 39 tests, guarded fresh kernels/references, fresh standalone/no-dev recreation, seeded UI regression, shared regression, local app browser checks, five local Mermaid illustrations, offline browser preview review (task 3.7), and Linux Podman build/runtime; [instructor record](classes/06-deployment/INSTRUCTOR.md), [tasks](openspec/changes/author-class-06-deployment/tasks.md) | Actual VS Code desktop: task 3.6; hosted authorization/build/CI/public URL/later release/peer handover, optional live model and platform/beginner trials pending; course files published in `705efd3` |

Classes 01–06 each allocate 90 classroom and 210 independent minutes. The first three parts contain interim exercises after approximately 20 minutes of teaching; each notebook has its own explicit starting assets/imports. Class 04 follows the approved simplified scope: architecture and a supplied FastAPI service, core HTTP consumption/failures, and short AI previews; pagination/retry implementation and new server development are optional. Class 05 supplies all validation, SDK handling, tools, and orchestration; required student edits are individual expressions/lines, with trace inspection and evaluation. Class 06 continues tiny edits with supplied UI/workflow/tests/configuration and separate student repository roots; its agreed preparation is 45 minutes, followed by 60 deployment, 60 CI, 30 logs/docs, and 15 peer handover. The separate instructor-designed project remains additional workload.

## Verification evidence and limits

- The shared verifier passed the template/specimen and authored classes 01–05, including fresh kernels, independent references, navigation, budgets, clean loaders, and the `%load` replacement protocol. Authored-class checks use each class's own environment. The class-04 regression run blocked real Requests session calls in notebooks/reference subprocesses.
- The six illustrations added to classes 01–02 were checked in rendered notebook previews, with local image loading, captions, credits, alternative text, white display backgrounds, and clean release cells. The [class-01](classes/01-oop-and-schemas/IMAGE_SUGGESTIONS.md) and [class-02](classes/02-reproducible-python-projects/IMAGE_SUGGESTIONS.md) guides record individual sources/licenses. At the published baseline, the [class-03 guide](classes/03-git-collaboration-and-testing/IMAGE_SUGGESTIONS.md) contained suggestions only; the local 20 November follow-up adds four embedded visuals.
- VS Code desktop interaction remains unverified because the available UI tools did not expose the desktop editor. Keep the seven corresponding OpenSpec tasks unchecked and the changes unarchived until actual desktop checks pass. Static previews and kernel protocol checks are separate evidence.
- Verification was performed on Linux/CPU. Windows examples have not been executed on Windows. Timings are internally checked allocations, not measured beginner trials; cross-platform setup and student timing trials remain delivery work.
- Class 04's actual World Bank snapshot and localhost Requests exchange were verified separately from its deterministic tests. Its AI fixtures are hand-authored illustrative envelopes; live model access/cost/performance was not tested. Five HTML exports passed structural inspection, but browser visual review remains pending because browser/app inventories were empty. Class-04 materials were committed and pushed in `a08a152`; images and visual/editor work remain outstanding.
- Class 04's independent standards/spec review found one P3 Bash-label issue, now corrected, and no confirmed spec violations. Its public-data reference now demonstrates the missing-value rejection required by the exercise. All 15 tests, Ruff, and all five notebooks/six references passed after the corrections. Three optional CC image suggestions have verified creators/licenses and notebook placement notes; direct downloads were rate-limited, so actual image rendering is not claimed.

- Class 05 was committed as `568bcaa` and pushed to `origin/main` on **19 November 2026**. All 32 tests and five notebooks/six references pass with real HTTP forbidden; the installed OpenAI SDK was exercised only through replaced HTTP transport. A third-execution regression was caught by an unchanged dispatch-spy test and passed after restoration. A fresh copied folder recreated its locked environment using a populated cache. All five HTML exports passed structural inspection; actual browser review was blocked by the in-app browser's local-file URL policy. VS Code desktop, live model/demo or recording, optional CPU Ollama capability/performance, platform setup, and beginner timing evidence remain pending. The glossary, one-field answer schema, fixed illustrative replays, two-execution/three-request limits, and tiny student completions match the approved interview.
- **20 November implementation assessment:** Class 05 implementation is complete against its approved scope. All 32 tests, Ruff lint/format checks, five fresh-kernel notebooks, six independent references, 90/210-minute budgets, release-state/navigation checks, and the `%load` kernel protocol passed again. The tests block real HTTP transport; this initial notebook rerun did not use the earlier external HTTP guard. The subsequent full class-06 integration regression did use the guard across all classes. Jupyter required permission for local kernel sockets. No class-05 browser/desktop, live-model, platform, beginner-timing, or new publication evidence was added. These separate pending delivery checks did not block class 06 authoring, which proceeded after the user confirmed both interview recommendations.
- **Class 06, 20 November:** the complete supplied distribution/OpenSpec is authored locally. All 39 tests and five notebooks/six references pass with real HTTP blocked, alongside Ruff, `%load` protocol, the 90/210-minute budgets, root workflow YAML checks, shared template/classes 01–06 regressions, and strict validation of all seven OpenSpec changes. A fresh standalone copy recreated from the populated cache, retained hidden root workflow/ignore files, excluded secrets/venvs from scratch staging, passed all tests, detected a seeded session-limit regression, and ran the real UI without dev dependencies. The local running app was inspected in the browser; five HTML exports passed structural checks, but browser file access was denied. Rootless Podman 4.9.3 built and ran the optional image on Linux/amd64, with saved-data/replay checks and loopback health verified. No public app, hosted CI, live model, peer handover, VS Code interaction, or course publication is claimed; platform/beginner trials remain pending.

## Course-wide review follow-up — 20 November 2026

The user approved the overall six-class review and its implementation while
preserving six weeks and 90 classroom/210 independent minutes per week. The
[curriculum](COURSE_REDESIGN.md#conceptual-difficulty-and-visual-scaffolding) now
records the main beginner bottlenecks: state/contracts, interpreter/kernel
identity, local/remote Git and fixtures, layered HTTP/data checks, bounded tool
round trips, and separate CI/hosting locations. Weeks 3 and 5 remain the largest
conceptual risks; week 6 has the greatest operational uncertainty. These are
source-review judgments, not measured beginner timings.

**Implemented locally:** corrected annotation/caption and exercise-direction
prose, inheritance placement, class-local environment guidance, cloning route,
and global classroom clocks. Week 3 reserves 15 of its existing 45 peer-review
minutes for an actual hosted PR/review or the same later catch-up slot; an
offline packet gives provisional completion only. The application scratch copy
is prepared before the ten-minute debugging exercise. Week 4 bridges the two
input-replacement APIs and explicitly documents the population parser's query-
completeness limit. Week 5 retains **build a small AI harness from supplied
components**, with a one-line validated-input change and observed successful/
absent/rejected behavior; loop, tools, and validation remain supplied. Week 6
wording now matches its diagnostic/documentation exercise.

**Images implemented:** 24 additional visuals, bringing the total to **30**:
classes 01/02 have six each, 03/04 four each, and 05/06 five each. Two new reused
images have source-verified CC BY-SA licenses; 22 are original course-specific
Mermaid diagrams with editable `.mmd` sources and CC BY 4.0 credits. Existing
six images remain. Every image is a local PNG with alt text, caption, and nearby
credit; each class's IMAGE_SUGGESTIONS.md records provenance/license information.
Students need no network image host or renderer. No legacy material was added.

**Automated/static verification:** template/specimen and all six classes passed
fresh kernels, independent references, clean release/navigation/loaders,
`%load` replacement protocol, and unchanged budgets with real Requests/HTTPX/
urllib transport blocked. Existing application suites passed **100 tests**
(class 02: 4; 03: 10; 04: 15; 05: 32; 06: 39), plus eight separately targeted
reference tests (03: 6; 04: 2). Ruff lint/format checks passed. All 30 notebook
exports embed their images; PNG paths/signatures/dimensions and alt text passed.
All seven OpenSpec changes passed strict validation. No application runtime
behavior was changed by the review.

**Browser verification:** local headless Chrome **157.0.8103.78**, with external
HTTP blocked, loaded all 30 HTML exports and all 30 images without page-wide
horizontal overflow. Actual image/caption/credit cells and the first exercise
card of each notebook were visually reviewed in browser screenshots; the tall
failure map was compacted and original diagrams use natural display dimensions.
The author-only renderer is Mermaid CLI **12.2.0** / Mermaid **12.3.0**; sources,
PNGs, and credits are bundled, while tooling and previews are under
`/tmp/adpro27-course-visuals`. This completes class-04 image/browser tasks 4.5/3.4
and class-05/06 static browser tasks 3.7. Earlier in-app file-URL restrictions
remain historical evidence, not the current browser-review status.

**Still separate/pending:** actual VS Code desktop interaction, supported-platform
and beginner timing trials, hosted GitHub PR/authentication, hosted deployment/
CI/peer handover, and live-model/Ollama delivery checks. The complete class-06
distribution and course-wide follow-up were committed as `705efd3` and pushed
to `origin/main` on **20 November 2026**, after the user explicitly requested
commit/push. Publication does not complete those pending delivery checks.

## Root navigation follow-up — 20 November 2026

Added a minimal [root README](README.md) linking to all six class guides. Static
verification confirmed each guide exists and is linked once, in course order.
Published in `3b9173b`, pushed to `origin/main` on **20 November 2026** after the
user requested commit/push. Lesson execution and delivery evidence are unchanged.

## Next work

1. When desktop access is available, run the pending VS Code checks on temporary copies, preserving an answer-cell sentinel while revealing and separately executing a reference. Record actual editor/extension versions and results before completing those tasks.
2. Complete class 04's separate VS Code desktop checks when UI access is available. Images and static browser review passed in the local 20 November follow-up. Recheck public endpoint/usage conditions and live instructor AI configuration before delivery; required AI work remains replay-based.
3. Complete class 05's pending VS Code desktop and instructor live-model demonstration or genuine recording, checking the exact model/feature combination separately from replay and mocked SDK tests. Test a CPU Ollama model before recommending it. Class 05 is published in `568bcaa`; its pending delivery checks remain separate.
4. Rehearse class 06's actual student GitHub authorization, hosted Actions for a subsequent commit, Community Cloud Python/dependency build, public no-AI URL/later release, and peer handover. Complete the separate VS Code desktop checks when available; static HTML browser review is now complete. Optional live AI requires private hosting and separately verified model/access/cost evidence; Linux Podman evidence does not cover macOS/Windows. Class 06 course files are published in `705efd3`; the actual student hosting rehearsal remains pending.
5. Complete supported-platform setup checks, beginner timing trials, and navigation/assessment-topic alignment before delivery. The instructor owns project design and assessment policy.

## Legacy content and record maintenance

The [repository guidance](AGENTS.md) defines the legacy rule: track material only when actually reused here. Root legacy directories are ignored by [.gitignore](.gitignore); none of their files were tracked at this update. The blueprint's reuse map is a local inventory, not evidence of completed migration or permission to stage those trees. Prefer adapting selected reused files into active class folders with provenance and required credits.

After completing a task, update its OpenSpec checklist and the relevant instructor verification record, then update this page if delivery status or next work changes. Record publication only after the corresponding commit and push succeed. Preserve pending checks and their concrete limitations.
