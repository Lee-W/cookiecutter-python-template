from __future__ import annotations

import subprocess

import pytest


def run_cmd(cmd: str) -> tuple[bytes, bytes, int]:
    process = subprocess.Popen(
        cmd,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        stdin=subprocess.PIPE,
    )
    stdout, stderr = process.communicate()
    return_code = process.returncode
    return stdout, stderr, return_code


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


@pytest.mark.parametrize("use_strict_mypy_config", ["n", "y"])
@pytest.mark.parametrize("python_version", ["3.9", "3.10", "3.11", "3.12", "3.13"])
@pytest.mark.parametrize("dependency_management_tool", ["poetry", "pipenv"])
@pytest.mark.parametrize("default_branch", ["main", "master"])
@pytest.mark.parametrize("build_pypi_package", ["n", "y"])
@pytest.mark.parametrize("build_docker_image", ["n", "y"])
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
@pytest.mark.parametrize("use_strict_mypy_config", ["n", "y"])
@pytest.mark.parametrize("python_version", ["3.9", "3.10", "3.11", "3.12", "3.13"])
@pytest.mark.parametrize("dependency_management_tool", ["poetry", "pipenv"])
@pytest.mark.parametrize("default_branch", ["main", "master"])
@pytest.mark.parametrize("build_pypi_package", ["n", "y"])
@pytest.mark.parametrize("build_docker_image", ["n", "y"])
def test_project_setup(
    cookies,
    default_context,
    build_docker_image,
    build_pypi_package,
    default_branch,
    dependency_management_tool,
    python_version,
    use_strict_mypy_config,
):
    result = cookies.bake(extra_context=default_context)
    context = default_context
    context["build_docker_image"] = build_docker_image
    context["build_pypi_package"] = build_pypi_package
    context["default_branch"] = default_branch
    context["dependency_management_tool"] = dependency_management_tool
    context["python_version"] = python_version
    context["use_strict_mypy_config"] = use_strict_mypy_config

    assert result.exit_code == 0
    assert result.exception is None

    with result.project.as_cwd():
        _, __, exit_code = run_cmd(f"{dependency_management_tool} run inv env.init-dev")
        assert exit_code == 0

        _, __, exit_code = run_cmd(f"{dependency_management_tool} run inv style")
        assert exit_code == 0

        run_cmd("git add .")
        _, __, exit_code = run_cmd(
            f"SKIP=no-commit-to-branch {dependency_management_tool} run pre-commit run --all-files"
        )
        assert exit_code == 0

        run_cmd(f"poetry env remove {python_version}")
