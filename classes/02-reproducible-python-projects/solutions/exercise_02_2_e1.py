"""02.2.E1: the interpreter path identifies which environment runs this cell."""

import importlib.metadata
import sys
import pydantic

print("Interpreter:", sys.executable)
print("Environment:", sys.prefix)
print("Base interpreter:", sys.base_prefix)
print("Pydantic:", importlib.metadata.version("pydantic"))
print("Package location:", pydantic.__file__)
assert sys.prefix != sys.base_prefix
# Expected: paths within the selected class .venv and its Pydantic installation.
# Compare with the scratch interpreter, not merely the Python version number.
# POSIX: .venv/bin/python -m pip --version
# Windows: .\.venv\Scripts\python.exe -m pip --version
# A terminal's installation command does not change the notebook kernel.
