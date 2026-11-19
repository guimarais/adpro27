# Course redesign execution status

Updated **19 November 2026**. This page tracks delivery of the [agreed curriculum](COURSE_REDESIGN.md); each linked OpenSpec checklist retains the detailed tasks. Implementation, verification, and publication are separate states.

## Published baseline

- `aaaf0f7`: curriculum redesign and content-template specification.
- `11dc49e`: VS Code teaching template/specimen and complete class 01.
- `04bd438`: complete classes 02–03, illustrations for classes 01–02, class-03 image suggestions, and related specifications/shared verification updates. Pushed to `origin/main` on 19 November 2026.
- `a08a152`: class 04 API lessons, reviewed examples, course execution/authoring records, and explicit pending-image work. Pushed to `origin/main` on 19 November 2026. Image download/embedding/visual review remains outstanding in task 4.5.

These commits identify the published course-material baseline. Publication records describe successful pushes; pending implementation and visual/editor checks retain their separate status.

## Delivery by block

| Area | Implemented and checked | Still outstanding |
| --- | --- | --- |
| [Template and specimen](templates/class-content/AUTHORING.md) | VS Code workspace/setup, notebook/Python/Markdown conventions, exercise cards, commented `%load`, fresh-kernel and static checks; [tasks](openspec/changes/add-course-content-template/tasks.md) | Desktop reveal interaction and visual checks: tasks 5.4–5.5 |
| [01 — OOP and schemas](classes/01-oop-and-schemas/README.md) | Five ordered notebooks, seven references, schemas/serialization, three local CC/CC0 illustrations; automated/protocol/static checks recorded in [instructor notes](classes/01-oop-and-schemas/INSTRUCTOR.md); [tasks](openspec/changes/author-class-01-oop-and-schemas/tasks.md) | Actual VS Code desktop check: task 5.6 |
| [02 — Reproducible Python projects](classes/02-reproducible-python-projects/README.md) | Five ordered notebooks, six references, complete local package, pip/venv/uv practice, four application checks, Ruff, fresh-copy recreation, three local CC illustrations; [instructor notes](classes/02-reproducible-python-projects/INSTRUCTOR.md); [tasks](openspec/changes/author-class-02-reproducible-python-projects/tasks.md) | Actual VS Code desktop check: task 3.6 |
| [03 — Git, collaboration, and testing](classes/03-git-collaboration-and-testing/README.md) | Five ordered notebooks, six references, passing default suite (10 tests), separately targeted reference (6 tests), seeded-bug/patch correction checks, isolated Git workflows, three CC image suggestions; [instructor notes](classes/03-git-collaboration-and-testing/INSTRUCTOR.md); [tasks](openspec/changes/author-class-03-git-collaboration-and-testing/tasks.md) | Actual VS Code desktop check: task 3.6; author checks did not exercise a hosted GitHub PR/authentication flow |
| [04 — Consuming APIs](classes/04-consuming-apis/README.md) | Five ordered notebooks, six references, supplied FastAPI service, minimal Requests client, World Bank mapping/snapshot, illustrative OpenAI/Ollama previews; 15 default tests + 2 reference checks, fresh kernels with HTTP blocked, real localhost/public smoke tests, fresh-copy recreation, Ruff and strict OpenSpec; [content review and two corrections](classes/04-consuming-apis/REVIEW.md), [three CC diagram suggestions](classes/04-consuming-apis/IMAGE_SUGGESTIONS.md); [instructor record](classes/04-consuming-apis/INSTRUCTOR.md), [tasks](openspec/changes/author-class-04-consuming-apis/tasks.md) | **Images pending:** download, embed, and visually inspect selected assets (task 4.5); downloads returned HTTP 429. Browser visual review of five HTML previews: task 3.4; actual VS Code desktop interaction: task 3.6; live AI/model and cross-platform delivery checks remain separate |
| 05 — Small AI applications | Curriculum, OpenAI primary path, replay fallback, and optional CPU Ollama direction agreed | OpenSpec and full class distribution not authored; verify provider/model details during authoring |
| 06 — Deployment and automated delivery | Curriculum, GitHub-connected hosting direction, and optional Podman extension agreed | OpenSpec and full class distribution not authored; deployment/CI/platform verification remains |

Classes 01–04 each allocate 90 classroom and 210 independent minutes. The first three parts contain interim exercises after approximately 20 minutes of teaching; each notebook has its own explicit starting assets/imports. Class 04 follows the approved simplified scope: architecture and a supplied FastAPI service, core HTTP consumption/failures, and short AI previews; pagination/retry implementation and new server development are optional. The separate instructor-designed project remains additional workload.

## Verification evidence and limits

- The shared verifier passed the template/specimen and authored classes 01–04, including fresh kernels, independent references, navigation, budgets, clean loaders, and the `%load` replacement protocol. Authored-class checks use each class's own environment. The class-04 regression run blocked real Requests session calls in notebooks/reference subprocesses.
- The six illustrations added to classes 01–02 were checked in rendered notebook previews, with local image loading, captions, credits, alternative text, white display backgrounds, and clean release cells. The [class-01](classes/01-oop-and-schemas/IMAGE_SUGGESTIONS.md) and [class-02](classes/02-reproducible-python-projects/IMAGE_SUGGESTIONS.md) guides record individual sources/licenses. The [class-03 guide](classes/03-git-collaboration-and-testing/IMAGE_SUGGESTIONS.md) contains suggestions, rather than embedded image assets.
- VS Code desktop interaction remains unverified because the available UI tools did not expose the desktop editor. Keep the five corresponding OpenSpec tasks unchecked and the changes unarchived until actual desktop checks pass. Static previews and kernel protocol checks are separate evidence.
- Verification was performed on Linux/CPU. Windows examples have not been executed on Windows. Timings are internally checked allocations, not measured beginner trials; cross-platform setup and student timing trials remain delivery work.
- Class 04's actual World Bank snapshot and localhost Requests exchange were verified separately from its deterministic tests. Its AI fixtures are hand-authored illustrative envelopes; live model access/cost/performance was not tested. Five HTML exports passed structural inspection, but browser visual review remains pending because browser/app inventories were empty. Class-04 materials were committed and pushed in `a08a152`; images and visual/editor work remain outstanding.
- Class 04's independent standards/spec review found one P3 Bash-label issue, now corrected, and no confirmed spec violations. Its public-data reference now demonstrates the missing-value rejection required by the exercise. All 15 tests, Ruff, and all five notebooks/six references passed after the corrections. Three optional CC image suggestions have verified creators/licenses and notebook placement notes; direct downloads were rate-limited, so actual image rendering is not claimed.

## Next work

1. When desktop access is available, run the pending VS Code checks on temporary copies, preserving an answer-cell sentinel while revealing and separately executing a reference. Record actual editor/extension versions and results before completing those tasks.
2. Complete class 04's pending images: download/embed selected diagrams with credits and alternative text, then inspect their actual rendered/offline display (task 4.5). Review the exported HTML previews and complete the separate VS Code desktop checks when UI access is available. Recheck public endpoint/usage conditions and live instructor AI configuration before delivery; required AI work remains replay-based.
3. Author class 05 and then class 06 against the blueprint, building on class 04's stable Observation interface and introductory HTTP AI examples. Recheck live API/SDK/model/hosting details at authoring time. Keep paid/live services optional for required exercise completion.
4. Complete supported-platform setup checks, beginner timing trials, and navigation/assessment-topic alignment before delivery. The instructor owns project design and assessment policy.

## Legacy content and record maintenance

The [repository guidance](AGENTS.md) defines the legacy rule: track material only when actually reused here. Root legacy directories are ignored by [.gitignore](.gitignore); none of their files were tracked at this update. The blueprint's reuse map is a local inventory, not evidence of completed migration or permission to stage those trees. Prefer adapting selected reused files into active class folders with provenance and required credits.

After completing a task, update its OpenSpec checklist and the relevant instructor verification record, then update this page if delivery status or next work changes. Record publication only after the corresponding commit and push succeed. Preserve pending checks and their concrete limitations.
