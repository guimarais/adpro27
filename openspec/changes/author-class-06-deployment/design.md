## Context

Class 05 implementation passed reassessment, while distinct delivery checks remain
pending. The curriculum authorizes class 06 authoring. On 20 November the user
confirmed tiny edits with supplied UI/workflow/tests/configuration and complete
class contents at the root of a separate student GitHub repository.

## Goals / Non-Goals

Goals: run a thin supplied UI, deploy from GitHub, diagnose one failure, configure
without committed secrets, inspect exact-commit checks, and hand over a public app
usable without AI credentials. Preserve the workload and truthful evidence.

Non-goals: new business logic, new harness/test suite/UI implementation by students,
workflow YAML from memory, CI-gated deployment infrastructure, anonymous paid AI,
GPU/local-model setup, new assessment policy, or automatically publishing course work.

## Decisions

### Distribution and reuse

Five standalone notebooks, six complete local references, class workspace, and
local uv metadata/lockfile. Reuse only active class-05 package/fixtures/harness
tests with provenance. The complete starter/reference app works without answers.
UI code imports existing loading, validation, summary, and bounded AI functions.
No new backend/API or generic provider/configuration framework is needed.

### Student root and runtime

The course retains classes/06-deployment, but students copy its contents to a
separate repository root outside the checkout, including hidden files. This
places workflow discovery, entrypoint, manifest, and lockfile where the supplied
instructions expect them. Python 3.13 is explicit in the local pin/manifest and
hosting instructions; CI reads the pin. No competing requirements route is added.

### Student activity and timing

Exercises change one title line, one entrypoint filename/diagnosis, one release
line, one workflow test command, and short diagnostic/handover notes. No blank
functions or new tests are required. First three parts each have 30 classroom/10
independent minutes; part 4 has 90 independent, part 5 has 45. Preparation adds 45.
Independent categories remain 45 preparation, 60 deployment, 60 CI, 30 logs/docs,
15 peer handover. Optional AI 45 plus Podman 135 is separate and at most 180.

### UI and configuration

Default UI shows saved 2023 observations, country selection/total, explicit absence,
attribution, release caption, and a labelled optional illustrative replay. Missing
AI settings leave that useful app intact. Live settings use a nested Streamlit
secrets table, explicit true flag, verified model/key, and a private access code.
The provider constructor accepts explicit values without modifying shared process
environment. One browser-session run and class-05 bounds limit each demonstration.
Hosting must also be private before optional live use. The classroom gate is not
identity or a durable/global spending cap; a new session can run again. Logs use
safe events/types/counters and never raw credential/provider exception bodies.

### Delivery and CI

One supplied student Actions job checks pushes and PRs, installs uv/selected Python,
syncs the lock, and runs offline tests plus Ruff lint/format checks. No live service
or model download runs in tests. Initial installation still needs network. Hosting
updates independently of CI; this lesson does not implement a deployment gate.
Supplied invented failure logs support practice while builds/access are pending,
but actual completion requires public URL, exact-commit passing CI for a later
change, visible release, and actual peer handover.

### Optional packaging

One short Containerfile packages runtime dependencies and app/fixtures. Explicit
COPY paths and container ignores exclude secrets/venvs. A loopback-mapped port
tests local execution, not public hosting. Platform-specific VM prerequisites
and setup/download time are included. Verify actual build/run independently.

## Risks / Trade-offs

- Account authorization/build delays: prepare within budget; offer saved diagnostics
  without falsely completing hosted tasks.
- Wrong root or Python: show exact inputs and verify actual logs/fresh standalone copy.
- UI reruns/session resets: no model requests occur without explicit button actions;
  document that the optional live cap is per session, not a global budget.
- Beginner overload: supply code, keep edits tiny, trial timing before teaching.
- Mock/static success can look like delivery: keep browser/editor, hosted/live,
  platform/peer, and publication evidence separate and pending when unavailable.

## Open Questions

No user design decision remains after confirmation. Actual hosting/account access,
live-model compatibility, desktop UI, optional container/platform support, and
beginner timing require concrete verification evidence.
