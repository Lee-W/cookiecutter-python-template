from invoke import task

from tasks.common import PIPENV_PREFIX


@task(default=True)
def run(ctx):
    """Run test cases"""
    ctx.run(f"{PIPENV_PREFIX} pytest", pty=True)


@task
def cov(ctx):
    """Run test covreage check"""
    ctx.run(f"{PIPENV_PREFIX} pytest --cov={{ cookiecutter.project_slug }} tests/", pty=True)
