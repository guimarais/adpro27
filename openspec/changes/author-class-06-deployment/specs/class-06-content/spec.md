## ADDED Requirements

### Requirement: Complete standalone class-six distribution
The class SHALL provide five ordered fresh-kernel notebooks, six explained
references, class-local workspace/environment/lockfile, supplied app/package/tests,
saved fixtures, and root-layout student deployment instructions. Required student
changes SHALL remain individual lines/settings and short written evidence.

#### Scenario: Student starts with guided practice
- **WHEN** part 06.4 runs from the installed complete folder
- **THEN** its own imports and local diagnostics work without earlier answers
- **AND** default notebook/reference execution starts no server, Git operation, or network request

### Requirement: Useful thin public data interface
The supplied Streamlit UI SHALL call existing Observation/data/summary functions,
show saved year/units/attribution and release, filter records, and distinguish
absent data from zero. The required application SHALL work without AI credentials.

#### Scenario: Visitor selects absent France
- **WHEN** FRA:2023 is selected
- **THEN** absence is explained and no invented numeric zero is displayed

### Requirement: Correct student root and reproducible hosting route
Students SHALL copy complete class contents including hidden files to a separate
repository root. Instructions SHALL align entrypoint, manifest/uv.lock, selected
Python minor, authentication, dependency/build logs, and actual public URL checks.
No competing dependency route SHALL be required.

#### Scenario: Student uses the supplied workflow
- **WHEN** class contents occupy the student repository root
- **THEN** .github/workflows/checks.yml is at repository-root discovery location
- **AND** streamlit_app.py and matching dependency metadata are at the documented hosting location

### Requirement: One supplied offline-checks workflow
One supplied job SHALL install the selected environment and run meaningful offline
tests plus lint/format checks for pushes/PRs without model credentials or downloads.
The class SHALL distinguish network installation from offline test behavior and
CI results from independent hosting updates.

#### Scenario: A change fails its automated check
- **WHEN** an Actions step fails
- **THEN** the student diagnoses that step and retains the check
- **AND** the lesson does not claim the failed check automatically blocks hosting

### Requirement: Safe optional live configuration and useful diagnostics
Default UI SHALL keep live AI disabled and preserve data/replay without settings.
Optional live use SHALL require private server configuration and access-code gate,
retain bounded execution and a small session run allowance, and document private
hosting requirements and the absence of a global cost guarantee. No unrestricted
instructor key SHALL be exposed through a required anonymous public feature.
Logs/UI errors SHALL avoid credential values and raw provider exception bodies.

#### Scenario: Optional AI configuration is incomplete
- **WHEN** live use is enabled without the required private settings
- **THEN** the app reports incomplete configuration without exposing values
- **AND** saved data and replay remain usable

### Requirement: Complete workload and actual handover evidence
The class SHALL allocate 90 classroom and 210 independent minutes, including
45 preparation, 60 deployment, 60 CI, 30 logs/docs, and 15 peer handover. The first
three parts SHALL contain 20+10 teaching/exercise cycles and 10 independent minutes
each, then 90 and 45 independent in parts 4–5. Completion SHALL require an actual
public no-AI URL, exact-commit passing check for a subsequent change, visible hosted
release, useful diagnostics, README, and peer result. Saved logs SHALL remain
explicitly illustrative practice, not hosted evidence.

#### Scenario: Hosting is unavailable during the exercise
- **WHEN** a student diagnoses the supplied log while a build/access is pending
- **THEN** the diagnostic result is recorded separately
- **AND** the public URL and hosted-check completion remain pending

### Requirement: Optional bounded Podman packaging
Optional work SHALL fit 180 separate minutes, with private AI up to 45 and local
Podman packaging up to 135 including setup/downloads. A supplied Containerfile
SHALL exclude local secrets/venvs, publish only a local test port in the guide,
and distinguish container execution from public hosting and platform verification.

#### Scenario: Student runs the optional container locally
- **WHEN** the documented loopback port mapping is used
- **THEN** it demonstrates local packaging only
- **AND** it is not recorded as a public deployment

### Requirement: Separate honest implementation and delivery verification
Author checks SHALL cover tests, fresh notebooks/references, clean release/loaders,
budgets/navigation, guarded offline behavior, regression detection, and fresh-copy
locked recreation. Static/headless checks, browser visual review, actual VS Code
interaction, hosted deployment/CI/peer handover, optional live/container, platform/
timing, and publication SHALL retain separate evidence. Unavailable checks SHALL
remain pending and publication SHALL require a successful explicit publication action.

#### Scenario: Only local tests and previews pass
- **WHEN** execution records are updated
- **THEN** hosted/desktop/live checks remain uncompleted unless actually performed


### Requirement: Offline teaching illustrations

The approved course-wide review SHALL be reflected in local teaching illustrations
(5 in this class), captions, meaningful alternative text, and source/license
records. Reused images SHALL retain file-specific credits and licenses. Original
course-specific diagrams SHALL retain editable Mermaid sources and CC BY 4.0
credits, alongside local PNG renderings. Images SHALL explain existing concepts
within the unchanged workload; their display SHALL NOT require network access or
a student-installed renderer.

#### Scenario: Student opens the complete class folder offline
- **WHEN** a notebook displays a teaching illustration
- **THEN** it reads the bundled PNG and supplies a textual explanation and credit
- **AND** editable source and license information are available locally or through the source guide
