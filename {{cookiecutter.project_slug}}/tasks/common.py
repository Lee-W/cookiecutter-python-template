from __future__ import annotations

VENV_PREFIX = "{{ cookiecutter.dependency_management_tool }} run"
_COMMON_TARGETS = ["{{ cookiecutter.project_slug }}", "tests", "tasks"]
COMMON_TARGETS_AS_STR = " ".join(_COMMON_TARGETS)
