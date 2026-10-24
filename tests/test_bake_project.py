import json
import os
import re
import shutil
import subprocess
import sys
import tomllib
from pathlib import Path
from unittest import mock

import pytest
import yaml

TRUE_AND_FALSE = (True, False)
SUPPORTED_BRANCH_NAMES = ("main", "master")
SUPPORTED_DEP_TOOLS = ("uv", "poetry", "pipenv")
SUPPORTED_TASK_RUNNERS = ("invoke", "poethepoet", "just")
# Only the oldest and the newest supported versions: the rendering does not differ in between
SUPPORTED_PYTHON_VERSIONS = ("3.11", "3.15")

# Entry point of each task runner in a baked project and how it spells a task name
RUNNER_ENTRYPOINTS = {
    "invoke": "{dep_tool} run inv {task}",
    "poethepoet": "{dep_tool} run poe {task}",
    "just": "just {task}",
}


HADOLINT_VERSION = json.loads((Path(__file__).parent.parent / "cookiecutter.json").read_text())[
    "_hadolint_version"
]

# GitHub Actions expressions (${{ ... }}) are legitimate in rendered workflows; just interpolations ({{ ... }}) in justfile
GITHUB_EXPRESSION = re.compile(r"\$\{\{.*?\}\}", re.DOTALL)
JUST_INTERPOLATION = re.compile(r"\{\{.*?\}\}", re.DOTALL)


def assert_no_template_leftovers(project_path: Path) -> None:
    for path in project_path.rglob("*"):
        if not path.is_file() or ".git" in path.relative_to(project_path).parts:
            continue
        try:
            text = path.read_text()
        except UnicodeDecodeError:
            continue
        text = GITHUB_EXPRESSION.sub("", text)
        if path.name == "justfile":
            text = JUST_INTERPOLATION.sub("", text)
        assert "{{" not in text, f"unrendered jinja expression in {path}"
        assert "{%" not in text, f"unrendered jinja block in {path}"


def assert_yaml_files_parse(project_path: Path) -> None:
    yaml_files = [
        *(project_path / ".github" / "workflows").glob("*.yaml"),
        project_path / ".pre-commit-config.yaml",
    ]
    assert yaml_files
    for yaml_file in yaml_files:
        assert yaml.safe_load(yaml_file.read_text()) is not None, yaml_file


def run_cmd(cmd: str) -> tuple[str, str, int]:
    process = subprocess.Popen(  # noqa: S602
        cmd,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        stdin=subprocess.PIPE,
    )
    stdout, stderr = process.communicate()
    return_code = process.returncode
    return stdout.decode("utf-8"), stderr.decode("utf-8"), return_code


@pytest.fixture
def default_context() -> dict[str, str]:
    return {
        "author_email": "author@example.com",
        "author_name": "author",
        "build_docker_image": "n",
        "build_pypi_package": "n",
        "default_branch": "main",
        "dependency_management_tool": "poetry",
        "task_runner": "invoke",
        "github_url": "https://github.com/author/test_python_project",
        "github_username": "author",
        "open_source_license": "GNU General Public License v3",
        "project_description": "Short Description for Python Project",
        "project_name": "Test Python Project",
        "project_slug": "test_python_project",
        "python_version": "3.11",
        "use_strict_mypy_config": "n",
    }


@pytest.mark.parametrize("use_strict_mypy_config", TRUE_AND_FALSE)
@pytest.mark.parametrize("python_version", SUPPORTED_PYTHON_VERSIONS)
@pytest.mark.parametrize("task_runner", SUPPORTED_TASK_RUNNERS)
@pytest.mark.parametrize("dependency_management_tool", SUPPORTED_DEP_TOOLS)
@pytest.mark.parametrize("default_branch", SUPPORTED_BRANCH_NAMES)
@pytest.mark.parametrize("build_pypi_package", TRUE_AND_FALSE)
@pytest.mark.parametrize("build_docker_image", TRUE_AND_FALSE)
def test_bake_project(
    cookies,
    default_context,
    build_docker_image,
    build_pypi_package,
    default_branch,
    dependency_management_tool,
    task_runner,
    python_version,
    use_strict_mypy_config,
):
    context = default_context
    context["build_docker_image"] = build_docker_image
    context["build_pypi_package"] = build_pypi_package
    context["default_branch"] = default_branch
    context["dependency_management_tool"] = dependency_management_tool
    context["task_runner"] = task_runner
    context["python_version"] = python_version
    context["use_strict_mypy_config"] = use_strict_mypy_config

    result = cookies.bake(extra_context=default_context)

    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_path.name == "test_python_project"
    assert result.project_path.is_dir()

    # Only the chosen task runner's files are kept
    assert (result.project_path / "tasks").exists() == (task_runner == "invoke")
    assert (result.project_path / "justfile").exists() == (task_runner == "just")
    pyproject = (result.project_path / "pyproject.toml").read_text()
    assert ("[tool.poe.tasks." in pyproject) == (task_runner == "poethepoet")

    # Everything rendered is syntactically valid and fully rendered
    assert tomllib.loads(pyproject)["project"]["name"]
    assert_yaml_files_parse(result.project_path)
    assert_no_template_leftovers(result.project_path)


@pytest.mark.parametrize("task_runner", SUPPORTED_TASK_RUNNERS)
@pytest.mark.parametrize("dependency_management_tool", SUPPORTED_DEP_TOOLS)
def test_bake_project_with_cruft_update(cookies, default_context, dependency_management_tool, task_runner):
    context = default_context
    context["dependency_management_tool"] = dependency_management_tool
    context["task_runner"] = task_runner
    context["auto_detect_update_from_cruft_template"] = True

    result = cookies.bake(extra_context=context)

    assert result.exit_code == 0
    assert result.exception is None
    cruft_workflow = result.project_path / ".github" / "workflows" / "cruft-update.yaml"
    assert cruft_workflow.exists()
    assert yaml.safe_load(cruft_workflow.read_text())
    assert_no_template_leftovers(result.project_path)


@pytest.mark.parametrize(
    ("dependency_management_tool", "build_pypi_package"),
    [("uv", True), ("uv", False), ("pipenv", True)],
)
def test_baked_invoke_tasks_are_lint_and_format_clean(
    cookies, default_context, dependency_management_tool, build_pypi_package
):
    context = default_context
    context["dependency_management_tool"] = dependency_management_tool
    context["build_pypi_package"] = build_pypi_package
    context["task_runner"] = "invoke"

    result = cookies.bake(extra_context=context)
    assert result.exit_code == 0

    config = result.project_path / "pyproject.toml"
    tasks_dir = result.project_path / "tasks"
    ruff = f"'{sys.executable}' -m ruff"
    for command in (
        f"{ruff} check --no-fix --no-cache --config '{config}' '{tasks_dir}'",
        f"{ruff} format --check --no-cache --config '{config}' '{tasks_dir}'",
    ):
        stdout, stderr, exit_code = run_cmd(command)
        print(stdout)
        print(stderr)
        assert exit_code == 0, command


def docker_available() -> bool:
    if shutil.which("hadolint"):
        return True
    return shutil.which("docker") is not None and run_cmd("docker info")[2] == 0


@pytest.mark.parametrize("dependency_management_tool", SUPPORTED_DEP_TOOLS)
def test_dockerfile_passes_hadolint(cookies, default_context, dependency_management_tool):
    if not docker_available():
        pytest.skip("neither hadolint nor a running docker is available")

    context = default_context
    context["dependency_management_tool"] = dependency_management_tool
    context["build_docker_image"] = True

    result = cookies.bake(extra_context=context)
    assert result.exit_code == 0

    dockerfile = result.project_path / "Dockerfile"
    if shutil.which("hadolint"):
        command = f"hadolint - < '{dockerfile}'"
    else:
        command = f"docker run --rm -i hadolint/hadolint:{HADOLINT_VERSION} < '{dockerfile}'"
    stdout, stderr, exit_code = run_cmd(command)
    print(stdout)
    print(stderr)
    assert exit_code == 0


@pytest.mark.slow
@pytest.mark.parametrize("task_runner", SUPPORTED_TASK_RUNNERS)
@pytest.mark.parametrize("dependency_management_tool", SUPPORTED_DEP_TOOLS)
@mock.patch.dict(os.environ, {"PIPENV_IGNORE_VIRTUALENVS": "1", "POETRY_VIRTUALENVS_IN_PROJECT": "true"})
def test_project_setup(
    cookies,
    default_context,
    dependency_management_tool,
    task_runner,
    monkeypatch,
):
    context = default_context

    version_info = sys.version_info
    context["python_version"] = f"{version_info[0]}.{version_info[1]}"
    context["build_docker_image"] = True
    context["build_pypi_package"] = True
    context["dependency_management_tool"] = dependency_management_tool
    context["task_runner"] = task_runner

    result = cookies.bake(extra_context=default_context)

    assert result.exit_code == 0
    assert result.exception is None

    monkeypatch.chdir(result.project_path)

    sep = "." if task_runner == "invoke" else "-"

    def run_task(task: str) -> str:
        return RUNNER_ENTRYPOINTS[task_runner].format(dep_tool=dependency_management_tool, task=task)

    for command in [
        run_task(f"env{sep}init-dev"),
        run_task("style"),
        f"git add . && SKIP=no-commit-to-branch,hadolint-docker {dependency_management_tool} run pre-commit run --all-files",
        run_task("test -a"),
        run_task(f"build{sep}dist"),
        run_task(f"env{sep}clean"),
    ]:
        stdout, stderr, exit_code = run_cmd(command)
        print(stdout)
        print(stderr)
        assert exit_code == 0

    assert list((result.project_path / "dist").glob("*.whl"))
