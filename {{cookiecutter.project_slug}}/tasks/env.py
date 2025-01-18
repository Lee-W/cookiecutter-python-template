from __future__ import annotations

from invoke.context import Context
from invoke.tasks import task

from tasks.common import VENV_PREFIX


@task
def clean(ctx: Context) -> None:
    """Remove virtual environment"""
    {% if cookiecutter.dependency_management_tool == "uv" -%}
    ctx.run("rm -rf .venv", warn=True)
    {%- elif cookiecutter.dependency_management_tool == "poetry" -%}
    ctx.run("poetry env remove {{ cookiecutter.python_version }}", warn=True)
    {%- elif cookiecutter.dependency_management_tool == "pipenv" -%}
    ctx.run("pipenv --rm", warn=True)
    {%- endif %}


@task
def init(ctx: Context) -> None:
    """Install production dependencies"""
    {% if cookiecutter.dependency_management_tool == "uv" -%}
    ctx.run("uv sync --no-dev")
    {%- elif cookiecutter.dependency_management_tool == "poetry" -%}
    ctx.run("poetry self add poetry-plugin-export")
    ctx.run("poetry install --no-dev")
    {%- elif cookiecutter.dependency_management_tool == "pipenv" -%}
    ctx.run("pipenv install --deploy")
    {%- endif %}


@task
def setup_pre_commit_hook(ctx: Context) -> None:
    """Setup pre-commit hook to automate check before git commit and git push"""
    ctx.run("git init")
    for hook_type in ("pre-commit", "pre-push", "commit-msg"):
        ctx.run(f"{VENV_PREFIX} pre-commit install -t {hook_type}")


@task(optional=["no-pre-commit"])
def init_dev(
    ctx: Context,
    groups_to_install: str = "dev,test,style,security,git",
    no_pre_commit: bool = False,
) -> None:
    """Install development dependencies and setup pre-commit hooks"""
    {% if cookiecutter.dependency_management_tool == "uv" -%}
    groups_args = " --group ".join(groups_to_install.split(","))
    groups_args = f"--group {groups_args}"
    ctx.run(f"uv sync {groups_args}")
    {%- elif cookiecutter.dependency_management_tool == "poetry" -%}
    ctx.run("poetry self add poetry-plugin-export")
    ctx.run(f"poetry install --with {groups_to_install}")
    {%- elif cookiecutter.dependency_management_tool == "pipenv" -%}
    ctx.run(f"pipenv install --categories {groups_to_install}")
    {%- endif %}
    if not no_pre_commit:
        setup_pre_commit_hook(ctx)
