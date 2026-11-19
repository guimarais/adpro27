## ADDED Requirements

### Requirement: Ordered class-three distribution

The class SHALL provide the five approved `03.1`–`03.5` notebooks, ordered navigation/index, a local uv environment/lockfile, and a VS Code workspace. Each notebook SHALL run with its own imports and explicit local assets from a fresh kernel, without previous student answers.

#### Scenario: Student starts with part 03.4
- **WHEN** the class is installed and part 03.4 is run fresh
- **THEN** its supplied fixture/test examples work without executing the earlier notebooks

### Requirement: Git basics begin the class

Part 03.1 SHALL introduce working tree, staging, local commits, status, unstaged/staged diffs, history, meaningful commit boundaries, and ignore rules. It SHALL distinguish Git from GitHub and use a separate practice repository with local identity configuration.

#### Scenario: Student prepares a commit
- **WHEN** the student follows the practice instructions
- **THEN** they inspect changes, stage intended files, inspect the staged snapshot, and commit without adding environment files or credentials

### Requirement: Branch and review workflow

Part 03.2 SHALL explain branches, merge, remotes, fetch/push/pull, and a GitHub pull-request workflow. It SHALL explain that pull fetches and integrates changes, not simply overwrites working files. It SHALL supply a review guide and clearly label any offline review equivalent.

#### Scenario: Online review access is unavailable
- **WHEN** a student uses the supplied review patch instead
- **THEN** the activity is labelled an offline review packet and does not claim to have created or published a GitHub PR

### Requirement: Safe default execution and recovery

Untouched notebooks and revealed reference files SHALL NOT initialize/mutate a Git repository, change global Git settings, push, contact GitHub, or read credentials. Git steps SHALL be explicit manual instructions. Recovery teaching SHALL use an ordinary prepared revert and a small conflict, not destructive reset commands. Instructor Git verification SHALL use isolated temporary repositories and local remotes.

#### Scenario: Instructor runs all notebooks
- **WHEN** default Run All completes
- **THEN** the course checkout and real Git history are unchanged and no remote operations have run

### Requirement: Meaningful pytest teaching

Part 03.3 SHALL demonstrate assertions about observable behavior, expected failures, and tests that detect a real seeded bug. Part 03.4 SHALL cover function-scoped fixtures, parametrization, and a small monkeypatch example at a supplied local input boundary. Normal imports SHALL work without sys.path modifications.

#### Scenario: Buggy mean is tested
- **WHEN** the intentionally wrong implementation is run against its explicit detecting tests
- **THEN** the expected test failure is visible and distinguished from collection/setup errors
- **AND** the corrected implementation passes the same checks in an isolated verification copy

### Requirement: Passing defaults and isolated broken examples

The supplied pytest configuration SHALL collect the passing `tests/` suite by default. Intentionally failing practice targets SHALL remain separate and explicitly labelled. Notebook demonstrations of such targets SHALL handle the expected nonzero result without hiding unexpected errors or making Run All fail.

#### Scenario: Student runs the default test command
- **WHEN** they run the documented pytest command from the class directory
- **THEN** the supplied reference suite passes and intentionally broken practice tests are not accidentally collected

### Requirement: Review and conflict judgment

Part 03.5 SHALL provide a small review diff introducing a behavioral regression and a conflict example. Its tasks SHALL require actionable review feedback, failure diagnosis, and a resolution consistent with the documented empty-data contract, rather than merely deleting markers or changing an assertion to match a bug.

#### Scenario: Reviewer sees the changed empty result
- **WHEN** they inspect the provided review patch
- **THEN** they can identify the regression, request a behavior test, and explain whether the change should be accepted

### Requirement: Complete workload and exercise chains

The index SHALL allocate 90 class minutes and 210 independent minutes: preparation 30; parts 03.1/03.2/03.3 each 30 class and 15 independent; part 03.4 60 independent; part 03.5 75 independent. The six chains SHALL be `03.1.E1`, `03.2.E1`, `03.3.E1`, `03.4.H1`, `03.5.H1`, and `03.5.H2`, with highlighted prompts, separate attempts, and exact commented local `%load` loaders. Checks/reflection SHALL be included in task times and project work additional.

#### Scenario: Student totals required work
- **WHEN** the index allocations are summed
- **THEN** the core block totals five hours without counting setup, exercises, or review twice

### Requirement: Creative Commons image suggestions

The class SHALL include an image-suggestion guide with at least three process diagrams, verified individual source-page URLs, creators, exact CC license names/links, attribution text, and suggested placements. It SHALL explain material terminology/scope caveats and provide text explanations so images/network access are optional.

#### Scenario: Instructor selects a diagram
- **WHEN** they open its suggestion
- **THEN** they can verify the image's own license, credit its creator, and identify the learning process it supports
- **AND** Commons' general metadata license is not presented as the image's license

### Requirement: Verified release with honest UI status

Verification SHALL cover structure, budgets, paths, clean loaders, fresh notebook execution, independent references, pytest/seeded failures, temporary Git workflows, and static presentation. Earlier class checks SHALL remain valid. Actual VS Code GUI checks SHALL be distinguished from protocol/static checks and remain pending if unavailable.

#### Scenario: Actual VS Code editor cannot be controlled
- **WHEN** only automated and static checks are possible
- **THEN** those results are recorded without claiming that a desktop GUI test passed
