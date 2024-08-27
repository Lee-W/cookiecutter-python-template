from __future__ import annotations

from invoke.context import Context
from invoke.tasks import task

from tasks.common import COMMON_TARGETS_AS_STR, VENV_PREFIX


@task
def ruff(ctx: Context) -> None:
    """Check style through ruff"""
    ctx.run(f"{VENV_PREFIX} ruff check {COMMON_TARGETS_AS_STR}")


@task
def mypy(ctx: Context) -> None:
    """Check style through mypy"""
    ctx.run(f"{VENV_PREFIX} mypy")


@task
def commit_check(ctx: Context, remote: str = "origin") -> None:
    """Check commit message through commitizen"""
    ctx.run(f"{VENV_PREFIX} cz -nr 3 check --rev-range {remote}/master..", warn=True)


@task(pre=[ruff, mypy, commit_check], default=True)
def run(ctx: Context) -> None:
    """Check style through linter"""
    pass


@task
def ruff_format(ctx: Context) -> None:
    """Format Python code through ruff"""
    ctx.run(f"{VENV_PREFIX} ruff format {COMMON_TARGETS_AS_STR}")


@task(pre=[ruff_format])
def format(ctx: Context) -> None:
    """Reformat python files through and ruff"""
    pass
