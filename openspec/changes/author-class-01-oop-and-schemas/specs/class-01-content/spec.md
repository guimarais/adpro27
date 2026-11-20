## ADDED Requirements

### Requirement: Ordered first-class notebooks

The class SHALL contain the five approved notebooks numbered `01.1` through `01.5` under `classes/01-oop-and-schemas/`, using the titles and order in the design. Its README SHALL link to every part in order. Every notebook SHALL identify its place in that sequence and link to the index and available neighboring parts.

#### Scenario: Student starts class 01
- **WHEN** the student opens the README
- **THEN** the student finds the five files in their required reading order and can identify in-class and independent activity

### Requirement: Fresh-kernel self-containment

Every notebook SHALL include its own imports, necessary small definitions, and inputs or explicitly included local fixture. It SHALL execute independently from a fresh kernel in the class directory without running another notebook, loading a reference solution, or completing a student answer. It SHALL NOT silently change directories, mutate `sys.path`, or require live external services.

#### Scenario: Student opens part 01.4 directly
- **WHEN** the student selects the supplied environment and runs part 01.4 from a fresh kernel
- **THEN** its demonstrations and checks succeed without variables from parts 01.1–01.3
- **AND** its recap explains the definitions and concepts needed to follow the file

### Requirement: Complete beginner-appropriate OOP coverage

Parts 01.1 and 01.2 SHALL explain classes, instances, attributes, constructors, methods, independent instance state, function-versus-method choices, and composition. They SHALL include brief, explicit inheritance and polymorphism examples without requiring advanced class hierarchies. Explanations SHALL connect code to observable outputs and common mistakes using the Report/Observation story.

#### Scenario: Student investigates shared state
- **WHEN** the student creates two reports and changes one
- **THEN** the lesson demonstrates the intended independence and explains the role of instance-owned mutable state

### Requirement: Schemas and validation coverage

Part 01.3 SHALL distinguish type hints from runtime checks and demonstrate Pydantic fields, constraints, missing/incorrect values, validation errors, default coercion, and a deliberate strict-field example. It SHALL use saved/local inputs and catch expected validation errors so the default Run All succeeds.

#### Scenario: Student validates a numeric string
- **WHEN** the student compares default validation with the strict-field example
- **THEN** the lesson shows whether the string is converted or rejected and explains why that policy differs from a type hint

### Requirement: Serialization and external contracts

Part 01.4 SHALL distinguish Python dictionaries, JSON text, instance serialization, and JSON Schema. It SHALL demonstrate serialization and round-trip validation and explain that a structural contract does not establish factual correctness or all application rules.

#### Scenario: Student compares exported data and schema
- **WHEN** the student exports an Observation and generates its JSON Schema
- **THEN** the student sees actual instance data separately from field/constraint descriptions

### Requirement: Integrated practice and review

Part 01.5 SHALL supply complete starting definitions and a local dataset, then require validation/collection, a small class/schema extension, and behavior checks/design reflection. Blank answer cells SHALL remain safe during Run All. Required checks and reflection SHALL be included in the stated exercise durations.

#### Scenario: Student has not finished an earlier exercise
- **WHEN** the student opens the practice notebook
- **THEN** its supplied baseline works and all tasks can be attempted without importing earlier student answers

### Requirement: Preserved weekly budget

The README SHALL allocate 90 in-class minutes and 210 independent minutes, including 30 minutes of preparation. Parts 01.1–01.3 SHALL each allocate 20 teaching minutes, ten interim exercise minutes, and 15 independent follow-up minutes. Parts 01.4 and 01.5 SHALL allocate 45 and 90 independent minutes respectively. Project work SHALL remain additional and optional extensions SHALL be excluded from required totals.

#### Scenario: Instructor totals required work
- **WHEN** the README allocations are summed
- **THEN** required work totals five hours without adding exercise, preparation, or reflection time twice

### Requirement: Lesson-specific exercise chains

The class SHALL provide `01.1.E1`, `01.2.E1`, `01.3.E1`, `01.4.H1`, and `01.5.H1`–`01.5.H3`. Each exercise SHALL have a prominent card with goal, duration/classification, starting point, task, expected completion, and hint; a separate answer cell; and a separate commented local `%load` cell. Prompt/answer/loader metadata SHALL carry the same full exercise ID. Every loader SHALL reference an existing `.py` file containing independent setup, explanation, and expected results.

#### Scenario: Student reveals exercise 01.2.E1
- **WHEN** the student uncomments its `%load` line
- **THEN** it references `solutions/exercise_01_2_e1.py` and uses a different cell from the student attempt
- **AND** the reference works without unfinished notebook answers

### Requirement: Class-local VS Code setup

The class SHALL include its own dependency manifest/lockfile and a class-root VS Code workspace with Python/Jupyter extension recommendations and a local `.venv` interpreter default. Setup instructions SHALL require no Git knowledge and SHALL explain notebook kernel selection and working-directory recovery. Each notebook SHALL check its local supporting paths and print the active interpreter path.

#### Scenario: Student downloads only the complete class folder
- **WHEN** the student follows its setup instructions
- **THEN** the five notebooks can run without the template/specimen directory or a browser notebook server

### Requirement: Multipart release verification

Verification SHALL check ordered filenames/navigation, class workspace, aggregate timing, unique full exercise IDs, supporting paths, valid nbformat, empty outputs/null counts, exact commented loaders, and absence of authoring placeholders. It SHALL execute every part in its own fresh kernel and verify reference solutions without student state. The original single-notebook template/specimen checks SHALL continue to pass. Protocol/source checks SHALL NOT be reported as VS Code GUI verification.

#### Scenario: One notebook contains an already loaded solution
- **WHEN** release verification inspects that notebook
- **THEN** verification rejects its altered loader source even if outputs have been cleared

#### Scenario: Actual desktop UI is unavailable
- **WHEN** only headless kernel and source checks can be performed
- **THEN** their results are recorded separately and the VS Code GUI checks remain pending


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
