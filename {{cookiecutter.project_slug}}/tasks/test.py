from __future__ import annotations

from invoke.context import Context
from invoke.tasks import task

from tasks.common import VENV_PREFIX


@task(default=True)
def run(ctx: Context, allow_no_tests: bool = False) -> None:
    """Run test cases"""
    result = ctx.run(f"{VENV_PREFIX} pytest", pty=True, warn=True)
    if allow_no_tests and result.exited == 5:
        exit(0)
    exit(result.exited)


@task
def cov(ctx: Context) -> None:
    """Run test coverage check"""
    ctx.run(f"{VENV_PREFIX} pytest --cov={{ cookiecutter.project_slug }} tests/", pty=True)
