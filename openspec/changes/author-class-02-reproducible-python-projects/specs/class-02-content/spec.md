## ADDED Requirements

### Requirement: Ordered independent class-two materials

The class SHALL provide the five approved `02.1`–`02.5` notebooks, a reading index, class-local uv environment/lockfile, and VS Code workspace. Each notebook SHALL have its own imports/setup and explicit local inputs, with no dependency on another notebook's state. Git knowledge SHALL NOT be required.

#### Scenario: Student opens part 02.3 directly
- **WHEN** the student follows the class setup and runs part 02.3 from a fresh kernel
- **THEN** its local demonstrations work without executing 02.1 or 02.2

### Requirement: Real module and entry-point teaching

Part 02.1 SHALL explain modules, packages, normal imports, the class working directory, import side effects, and a module entry point. A supplied local Report/Observation application SHALL run through `python -m report_app` and SHALL NOT run its CLI merely because a module is imported.

#### Scenario: Another program imports the example
- **WHEN** it imports the supplied modules
- **THEN** reusable definitions are available without unexpected CLI output or file processing

### Requirement: Environment and pip fundamentals

Part 02.2 SHALL explain interpreter selection, isolation, venv, pip tied to an interpreter, and package-location inspection. It SHALL give POSIX/Windows commands for a scratch environment, distinguish notebook kernel from terminal interpreter, and avoid modifying the system or teaching environment automatically.

#### Scenario: Student compares two environments
- **WHEN** the student follows the explicit interpreter commands
- **THEN** they can identify which Python owns an installation and distinguish the scratch environment from the notebook kernel

### Requirement: uv project workflow

Part 02.3 SHALL explain declared dependencies, resolved lockfiles, add/run/sync, and the difference from pip-style installation. It SHALL provide a no-Git scratch-project exercise and explain locked environment recreation. Notebook Run All SHALL NOT create environments or download packages.

#### Scenario: Student adds a dependency
- **WHEN** the student runs the documented uv commands in a disposable project
- **THEN** the project manifest and lockfile record the dependency and its resolution
- **AND** the learner can reproduce the run using the declared project rather than their global Python state

### Requirement: Readability and useful documentation

Part 02.4 SHALL teach naming, small functions, type hints, useful docstrings, and minimal run instructions. It SHALL supply Ruff with a small configuration, distinguish linting from formatting, and avoid presenting either as proof of correctness.

#### Scenario: Student improves a function
- **WHEN** they complete the quality exercise
- **THEN** its behavior remains explicit, its empty-data contract is documented, and its run/check instructions can be followed

### Requirement: Refactoring and recreation practice

Part 02.5 SHALL provide a complete monolithic refactoring starter and independent tasks to organize it into modules and recreate the environment in a fresh working copy. It SHALL require no completed earlier student answer. The required workload SHALL total 90 class and 210 independent minutes with exercises/review counted once and the project additional.

#### Scenario: Instructor checks the workload
- **WHEN** the index allocations are summed
- **THEN** the first three parts each have 20 teaching minutes plus ten exercise minutes and required independent work totals 210 minutes

### Requirement: Safe reference solutions and clean release

The class SHALL provide six exercise chains: `02.1.E1`, `02.2.E1`, `02.3.E1`, `02.4.H1`, `02.5.H1`, and `02.5.H2`. Each SHALL use a highlighted card, separate answer/loader cells, matching metadata, and an existing local `.py` reference. Terminal/file-editing steps SHALL be comments rather than automatically executed installation or mutation commands. Released notebooks SHALL have empty outputs, null counts, and exact commented loaders.

#### Scenario: Student runs the untouched notebook
- **WHEN** they use Run All
- **THEN** examples execute locally, empty answers do not fail, and references do not install dependencies, change files, or appear automatically

### Requirement: Verified application and teaching artifacts

Verification SHALL cover ordered navigation, workspace, budgets, IDs, links, fresh notebook execution, independent references, lint/format checks, application state/empty-data/CLI/import behavior, and locked recreation in a fresh working copy. It SHALL preserve class-01/template checks and distinguish actual VS Code GUI checks from kernel/protocol or static-preview checks.

#### Scenario: A fresh copy is prepared
- **WHEN** the documented locked environment is recreated and the application is run
- **THEN** its expected summary is produced without the original `.venv` or another notebook's state


### Requirement: Offline teaching illustrations

The approved course-wide review SHALL be reflected in local teaching illustrations
(6 in this class), captions, meaningful alternative text, and source/license
records. Reused images SHALL retain file-specific credits and licenses. Original
course-specific diagrams SHALL retain editable Mermaid sources and CC BY 4.0
credits, alongside local PNG renderings. Images SHALL explain existing concepts
within the unchanged workload; their display SHALL NOT require network access or
a student-installed renderer.

#### Scenario: Student opens the complete class folder offline
- **WHEN** a notebook displays a teaching illustration
- **THEN** it reads the bundled PNG and supplies a textual explanation and credit
- **AND** editable source and license information are available locally or through the source guide
