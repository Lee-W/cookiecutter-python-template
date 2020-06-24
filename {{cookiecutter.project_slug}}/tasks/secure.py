from invoke import task

from tasks.common import VENV_PREFIX


@task
def check_package(ctx):
    """Check package security"""
    {% if cookiecutter.dependency_management_tool == 'pipenv' -%}
    ctx.run("pipenv check")
    {%- elif cookiecutter.dependency_management_tool == 'poetry' -%}
    ctx.run("poetry run safety", warn=True)
    {%- endif %}


@task
def bandit(ctx):
    """Check common software vulnerabilities (Use it as reference only)"""
    ctx.run(f"{VENV_PREFIX} bandit -r -iii -lll --ini .bandit", pty=True)


@task(pre=[check_package, bandit], default=True)
def run(ctx):
    """Check security check throguh safety and bandit"""
    pass
