from invoke import task

from tasks.common import VENV_PREFIX


@task
def clean(ctx):
    """Remove virtual environement"""
    {% if cookiecutter.dependency_management_tool == 'pipenv' -%}
    ctx.run("pipenv --rm", warn=True)
    {%- elif cookiecutter.dependency_management_tool == 'poetry' -%}
    ctx.run("poetry env remove {{ cookiecutter.python_version }}", warn=True)
    {%- endif %}


@task
def init(ctx):
    """Install production dependencies"""
    {% if cookiecutter.dependency_management_tool == 'pipenv' -%}
    ctx.run("pipenv install --deploy")
    {%- elif cookiecutter.dependency_management_tool == 'poetry' -%}
    ctx.run("poetry install --no-dev")
    {%- endif %}


@task
def setup_pre_commit_hook(ctx):
    """Setup pre-commit hook to automate check before git commit and git push"""
    ctx.run("git init")
    ctx.run(
        f"{VENV_PREFIX} pre-commit install -t pre-commit & "
        f"{VENV_PREFIX} pre-commit install -t pre-push & "
        f"{VENV_PREFIX} pre-commit install -t commit-msg"
    )


@task(optional=["no-pre-commit"])
def init_dev(ctx, no_pre_commit=False):
    """Install development dependencies and setup pre-commit hooks"""
    {% if cookiecutter.dependency_management_tool == 'pipenv' -%}
    ctx.run("pipenv install --dev")
    {%- elif cookiecutter.dependency_management_tool == 'poetry' -%}
    ctx.run("poetry install")
    {%- endif %}
    if not no_pre_commit:
        setup_pre_commit_hook(ctx)
