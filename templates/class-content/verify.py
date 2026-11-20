"""Check release notebooks and execute fresh copies without writing outputs back."""

from pathlib import Path
import json
import re
import subprocess
import sys
from urllib.parse import unquote, urlsplit

import nbformat
from nbclient import NotebookClient
from jupyter_client import KernelManager


ROOT = Path(__file__).resolve().parent
LOADER = (
    "# Reveal only after attempting the exercise.\n"
    "# Remove the leading '# ' from the next line and run this cell.\n"
    "# %load solutions/{filename}"
)


def check_links(source, directory):
    """Check local Markdown targets; external references remain source links."""
    for target in re.findall(r"\]\(([^)]+)\)", source):
        url = urlsplit(target)
        if not url.scheme and url.path:
            assert (directory / unquote(url.path)).exists(), f"Broken link: {target}"


def verify(path):
    notebook = nbformat.read(path, as_version=4)
    nbformat.validate(notebook)
    part_match = re.fullmatch(r"(0[1-6])\.([1-9]\d*)-[a-z]+(?:-[a-z]+)*", path.stem)
    is_part = part_match is not None
    if is_part:
        assert path.parent.name.startswith(part_match[1] + "-"), path
    else:
        assert path.stem == path.parent.name, f"Class/notebook name mismatch: {path}"
    is_template = path.parent.name == "NN-topic"
    is_specimen = path == ROOT / "example/01-oop-and-schemas/01-oop-and-schemas.ipynb"
    class_number = "NN" if is_template else path.name[:2]
    if not is_template and not is_part:
        assert re.fullmatch(r"0[1-6]-[a-z]+(?:-[a-z]+)*", path.stem), path
    assert notebook.metadata.kernelspec.language == "python"
    workspace_path = path.parent / (path.parent.name + ".code-workspace") if is_part else path.with_suffix(".code-workspace")
    workspace = json.loads(workspace_path.read_text())
    assert workspace["folders"] == [{"path": "."}], "Open only the numbered class folder"
    assert workspace["settings"]["jupyter.notebookFileRoot"] == "${workspaceFolder}"
    assert {"ms-python.python", "ms-toolsai.jupyter"} <= set(workspace["extensions"]["recommendations"])
    environment = workspace["settings"]["python.defaultInterpreterPath"]
    assert environment.startswith("${workspaceFolder}/")
    environment_path = path.parent / environment.removeprefix("${workspaceFolder}/")
    assert (environment_path / "pyvenv.cfg").is_file(), environment
    exercise_cells = {}
    source = "\n".join(cell.source for cell in notebook.cells)
    assert not re.search(r"\{\{|\bAUTHOR:", source) or is_template, path

    for cell in notebook.cells:
        if cell.cell_type == "markdown":
            check_links(cell.source, path.parent)
        if cell.cell_type == "code":
            assert cell.outputs == [] and cell.execution_count is None, cell.id
        tags = set(cell.metadata.get("tags", []))
        roles = tags & {"exercise", "exercise-answer", "solution-loader"}
        if not roles:
            continue
        assert len(roles) == 1, cell.id
        role = roles.pop()
        exercise_id = cell.metadata["exercise_id"]
        exercise_cells.setdefault(exercise_id, []).append(role)
        if role == "exercise":
            assert cell.cell_type == "markdown" and f"Exercise {exercise_id}" in cell.source
            for label in ("Goal", "Start here", "Task", "Check", "Hint"):
                assert f"**{label}:**" in cell.source, (exercise_id, label)
        else:
            assert cell.cell_type == "code", cell.id
        if role == "solution-loader":
            number, *suffixes = exercise_id.split(".")
            filename = f"exercise_{number}_{'_'.join(s.lower() for s in suffixes)}.py"
            assert cell.source == LOADER.format(filename=filename), f"Restore loader: {exercise_id}"
            assert (path.parent / "solutions" / filename).is_file(), filename

    if is_part:
        lesson_id = path.stem.split("-", 1)[0]
        assert notebook.metadata.course_lesson.id == lesson_id
        assert exercise_cells and all(re.fullmatch(rf"{re.escape(lesson_id)}\.[EH][1-9]\d*", name) for name in exercise_cells)
    else:
        interim_ids = {exercise_id for exercise_id in exercise_cells if ".H" not in exercise_id}
        expected_interim = {f"{class_number}.{i}" for i in ([1] if is_specimen else [1, 2, 3])}
        assert interim_ids == expected_interim and f"{class_number}.H1" in exercise_cells
        assert all(re.fullmatch(rf"{class_number}\.(?:[1-3]|H[1-9]\d*)", name) for name in exercise_cells)
    assert all(roles == ["exercise", "exercise-answer", "solution-loader"] for roles in exercise_cells.values())
    if not is_specimen and not is_part:
        agendas = [c.source for c in notebook.cells if "class-agenda" in c.metadata.get("tags", [])]
        budgets = [c.source for c in notebook.cells if "independent-budget" in c.metadata.get("tags", [])]
        assert len(agendas) == len(budgets) == 1
        intervals = re.findall(r"^\| (\d+)–(\d+) \|", agendas[0], re.M)
        assert intervals == [("0", "20"), ("20", "30"), ("30", "50"), ("50", "60"), ("60", "80"), ("80", "90")]
        assert sum(map(int, re.findall(r"^\| (\d+) \|", budgets[0], re.M))) == 210

    # nbclient starts a fresh kernel; all execution changes stay in this object.
    NotebookClient(
        notebook,
        timeout=60,
        kernel_name="python3",
        resources={"metadata": {"path": str(path.parent)}},
        extra_arguments=["--HistoryManager.hist_file=:memory:"],
    ).execute()
    check_links((path.parent / "README.md").read_text(), path.parent)
    label = path.relative_to(ROOT) if path.is_relative_to(ROOT) else path
    print(f"PASS {label}: structure, VS Code workspace, release state, links, solutions, fresh Run All")
    return notebook


def verify_class(directory):
    """Check ordered parts together, then run each part/reference independently."""
    number = directory.name[:2]
    paths = sorted(directory.glob(f"{number}.*.ipynb"), key=lambda p: int(p.stem.split("-", 1)[0].split(".")[1]))
    assert paths, f"No ordered notebooks in {directory}"
    ids = [p.stem.split("-", 1)[0] for p in paths]
    assert ids == [f"{number}.{i}" for i in range(1, len(paths) + 1)], ids
    index = (directory / "README.md").read_text()
    rows = re.findall(r"^\| \[[^\]]+\]\(([^)]+\.ipynb)\) \| (\d+) \| (\d+) \|", index, re.M)
    assert [row[0] for row in rows] == [p.name for p in paths], "Index must list all parts once, in order"
    preparation = re.search(r"^\| Preparation and VS Code setup \| (\d+) \| (\d+) \|", index, re.M)
    preparation_minutes = 45 if number == "06" else 30
    assert preparation and tuple(map(int, preparation.groups())) == (0, preparation_minutes)
    assert sum(int(row[1]) for row in rows) == 90
    assert preparation_minutes + sum(int(row[2]) for row in rows) == 210
    exercises = set()
    for position, (path, row) in enumerate(zip(paths, rows)):
        notebook = verify(path)
        metadata = notebook.metadata.course_lesson
        assert (metadata.in_class_minutes, metadata.independent_minutes) == (int(row[1]), int(row[2]))
        navigation = notebook.cells[0].source
        assert "](README.md)" in navigation
        for neighbor in [position - 1, position + 1]:
            if 0 <= neighbor < len(paths):
                assert f"]({paths[neighbor].name})" in navigation, "Missing neighbor navigation"
        part_ids = {cell.metadata.exercise_id for cell in notebook.cells if "exercise" in cell.metadata.get("tags", [])}
        assert not exercises & part_ids, "Exercise IDs must be unique across parts"
        exercises.update(part_ids)
    if number in {"01", "02", "03", "04", "05", "06"}:
        assert len(paths) == 5
        allocations = [(30, 15), (30, 15), (30, 15), (0, 45), (0, 90)]
        if number in {"03", "04", "05"}:
            allocations = [(30, 15), (30, 15), (30, 15), (0, 60), (0, 75)]
        if number == "06":
            allocations = [(30, 10), (30, 10), (30, 10), (0, 90), (0, 45)]
        assert [(int(row[1]), int(row[2])) for row in rows] == allocations
        expected = {f"{number}.{i}.E1" for i in [1, 2, 3]} | {f"{number}.4.H1", f"{number}.5.H1", f"{number}.5.H2"}
        if number == "01":
            expected.add("01.5.H3")
        assert exercises == expected
    for exercise_id in sorted(exercises):
        filename = "exercise_" + exercise_id.replace(".", "_").lower() + ".py"
        subprocess.run([sys.executable, "-m", f"solutions.{Path(filename).stem}"], cwd=directory, check=True)
    for document in directory.glob("*.md"):
        check_links(document.read_text(), directory)
    print(f"PASS class {number}: ordered parts, 90/210-minute budget, unique IDs, independent references")


def verify_load_payload(directory=None, filename="exercise_01_1.py", result_name="reference_totals"):
    """Check IPython's replacement contract separately from VS Code GUI behavior."""
    directory = directory or ROOT / "example/01-oop-and-schemas"
    manager = KernelManager(kernel_name="python3")
    manager.start_kernel(cwd=str(directory), extra_arguments=["--HistoryManager.hist_file=:memory:"])
    client = manager.client()
    try:
        client.start_channels()
        client.wait_for_ready(timeout=30)
        reply = client.execute_interactive(f"%load solutions/{filename}", timeout=30)
        assert reply["content"]["status"] == "ok"
        payload = next(p for p in reply["content"]["payload"] if p["source"] == "set_next_input")
        assert payload["replace"] is True
        assert payload["text"].endswith((directory / "solutions" / filename).read_text())
        reply = client.execute_interactive(f"assert {result_name!r} not in globals()", timeout=30)
        assert reply["content"]["status"] == "ok", "Loading must not execute the solution"
        reply = client.execute_interactive(payload["text"], timeout=30)
        assert reply["content"]["status"] == "ok"
        reply = client.execute_interactive(f"assert {result_name!r} in globals()", timeout=30)
        assert reply["content"]["status"] == "ok"
        print("PASS %load replacement payload and separate execution (not a VS Code GUI test)")
    finally:
        client.stop_channels()
        manager.shutdown_kernel(now=True)


if __name__ == "__main__":
    paths = [Path(arg).resolve() for arg in sys.argv[1:]] or [
        ROOT / "NN-topic/NN-topic.ipynb",
        ROOT / "example/01-oop-and-schemas/01-oop-and-schemas.ipynb",
    ]
    if len(sys.argv) == 1:
        paths.extend(sorted((ROOT.parents[1] / "classes").glob("0[1-6]-*")))
    for path in paths:
        if path.is_dir():
            # Each distribution owns its dependencies (class 03 adds pytest).
            # Keep venv paths un-resolved: their executables may share a base symlink.
            executable = path / ".venv" / ("Scripts/python.exe" if sys.platform == "win32" else "bin/python")
            assert executable.is_file(), f"Run uv sync --locked in {path}"
            if executable.absolute() != Path(sys.executable).absolute():
                subprocess.run([str(executable), str(Path(__file__).resolve()), str(path)], check=True)
                continue
            verify_class(path)
            if path.name == "01-oop-and-schemas":
                verify_load_payload(path, "exercise_01_1_e1.py", "left")
            elif path.name == "02-reproducible-python-projects":
                verify_load_payload(path, "exercise_02_1_e1.py", "module_result")
            elif path.name == "03-git-collaboration-and-testing":
                verify_load_payload(path, "exercise_03_1_e1.py", "reference_plan")
            elif path.name == "04-consuming-apis":
                verify_load_payload(path, "exercise_04_1_e1.py", "reference_rows")
            elif path.name == "05-small-ai-applications":
                verify_load_payload(path, "exercise_05_1_e1.py", "reference_answer")
            elif path.name == "06-deployment":
                verify_load_payload(path, "exercise_06_1_e1.py", "reference_title")
        else:
            verify(path)
    if len(sys.argv) == 1:
        verify_load_payload()
    check_links((ROOT / "AUTHORING.md").read_text(), ROOT)
    print("PASS Markdown links")
