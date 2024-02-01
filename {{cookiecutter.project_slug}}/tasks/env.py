from invoke import task
from invoke.context import Context

from tasks.common import VENV_PREFIX


@task
def clean(ctx: Context) -> None:
    """Remove virtual environment"""
    {% if cookiecutter.dependency_management_tool == 'pipenv' -%}
    ctx.run("pipenv --rm", warn=True)
    {%- elif cookiecutter.dependency_management_tool == 'poetry' -%}
    ctx.run("poetry env remove {{ cookiecutter.python_version }}", warn=True)
    {%- endif %}


@task
def init(ctx: Context) -> None:
    """Install production dependencies"""
    {% if cookiecutter.dependency_management_tool == 'pipenv' -%}
    ctx.run("pipenv install --deploy")
    {%- elif cookiecutter.dependency_management_tool == 'poetry' -%}
    ctx.run("poetry install --no-dev")
    {%- endif %}


@task
def setup_pre_commit_hook(ctx: Context) -> None:
    """Setup pre-commit hook to automate check before git commit and git push"""
    ctx.run("git init")
    ctx.run(
        f"{VENV_PREFIX} pre-commit install -t pre-commit & "
        f"{VENV_PREFIX} pre-commit install -t pre-push & "
        f"{VENV_PREFIX} pre-commit install -t commit-msg &"
        f"{VENV_PREFIX} pre-commit autoupdate"
    )


@task(optional=["no-pre-commit"])
def init_dev(ctx: Context, no_pre_commit: bool = False) -> None:
    """Install development dependencies and setup pre-commit hooks"""
    {% if cookiecutter.dependency_management_tool == 'pipenv' -%}
    ctx.run("pipenv install --dev")
    {%- elif cookiecutter.dependency_management_tool == 'poetry' -%}
    ctx.run("poetry install")
    {%- endif %}
    if not no_pre_commit:
        setup_pre_commit_hook(ctx)
