from __future__ import annotations

import os
import subprocess
import sys
from unittest import mock

import pytest

TRUE_AND_FALSE = (True, False)
SUPPORTED_BRANCH_NAMES = ("main", "master")
SUPPORTED_DEP_TOOLS = ("uv", "poetry", "pipenv")
SUPPORTED_PYTHON_VERSIONS = ("3.9", "3.10", "3.11", "3.12", "3.13")


def run_cmd(cmd: str) -> tuple[str, str, int]:
    process = subprocess.Popen(
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
        "github_url": "https://github.com/author/test_python_project",
        "github_username": "author",
        "open_source_license": "GNU General Public License v3",
        "project_description": "Short Description for Python Project",
        "project_name": "Test Python Project",
        "project_slug": "test_python_project",
        "python_version": "3.9",
        "use_strict_mypy_config": "n",
    }


@pytest.mark.parametrize("use_strict_mypy_config", TRUE_AND_FALSE)
@pytest.mark.parametrize("python_version", SUPPORTED_PYTHON_VERSIONS)
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
    python_version,
    use_strict_mypy_config,
):
    context = default_context
    context["build_docker_image"] = build_docker_image
    context["build_pypi_package"] = build_pypi_package
    context["default_branch"] = default_branch
    context["dependency_management_tool"] = dependency_management_tool
    context["python_version"] = python_version
    context["use_strict_mypy_config"] = use_strict_mypy_config

    result = cookies.bake(extra_context=default_context)

    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_path.name == "test_python_project"
    assert result.project_path.is_dir()


@pytest.mark.slow
@pytest.mark.parametrize("use_strict_mypy_config", TRUE_AND_FALSE)
@pytest.mark.parametrize("dependency_management_tool", SUPPORTED_DEP_TOOLS)
@pytest.mark.parametrize("default_branch", SUPPORTED_BRANCH_NAMES)
@pytest.mark.parametrize("build_pypi_package", TRUE_AND_FALSE)
@pytest.mark.parametrize("build_docker_image", TRUE_AND_FALSE)
@mock.patch.dict(os.environ, {"PIPENV_IGNORE_VIRTUALENVS": "1", "POETRY_VIRTUALENVS_IN_PROJECT": "true"})
def test_project_setup(
    cookies,
    default_context,
    build_docker_image,
    build_pypi_package,
    default_branch,
    dependency_management_tool,
    use_strict_mypy_config,
    monkeypatch,
):
    context = default_context

    version_info = sys.version_info
    context["python_version"] = f"{version_info[0]}.{version_info[1]}"
    context["build_docker_image"] = build_docker_image
    context["build_docker_image"] = build_docker_image
    context["build_pypi_package"] = build_pypi_package
    context["default_branch"] = default_branch
    context["dependency_management_tool"] = dependency_management_tool
    context["use_strict_mypy_config"] = use_strict_mypy_config

    result = cookies.bake(extra_context=default_context)

    assert result.exit_code == 0
    assert result.exception is None

    monkeypatch.chdir(result.project_path)

    for command in [
        f"{dependency_management_tool} run inv env.init-dev",
        f"{dependency_management_tool} run inv style",
        f"git add . && SKIP=no-commit-to-branch,hadolint-docker {dependency_management_tool} run pre-commit run --all-files",
        f"{dependency_management_tool} run inv env.clean",
    ]:
        stdout, stderr, exit_code = run_cmd(command)
        print(stdout)
        print(stderr)
        assert exit_code == 0
