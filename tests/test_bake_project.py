import subprocess
from typing import Dict, Tuple

import pytest


def run_cmd(cmd: str) -> Tuple[bytes, bytes, int]:
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
def default_context() -> Dict[str, str]:
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
        "project_description": "Short Descirption for Python Project",
        "project_name": "Test Python Project",
        "project_slug": "test_python_project",
        "python_version": "3.7",
        "use_strict_mypy_config": "n",
    }


def test_bake_project(cookies, default_context):
    result = cookies.bake(extra_context=default_context)

    assert result.exit_code == 0
    assert result.exception is None
    assert result.project.basename == "test_python_project"
    assert result.project.isdir()


@pytest.mark.slow
def test_project_setup(cookies, default_context):
    result = cookies.bake(extra_context=default_context)

    assert result.exit_code == 0
    assert result.exception is None

    with result.project.as_cwd():
        _, __, exit_code = run_cmd("poetry run inv env.init-dev")
        assert exit_code == 0

        _, __, exit_code = run_cmd("poetry run inv style")
        assert exit_code == 0

        run_cmd("git add .")
        _, __, exit_code = run_cmd("poetry run pre-commit run --all-files")
        assert exit_code == 0

        run_cmd(f"poetry env remove {default_context['python_version']}")
