from __future__ import annotations

from invoke.context import Context
from invoke.tasks import task

from tasks.common import VENV_PREFIX


@task
def commit(ctx: Context) -> None:
    """Commit through commitizen"""
    ctx.run(f"{VENV_PREFIX} cz commit", pty=True)


@task
def bump(ctx: Context, changelog: bool = False) -> None:
    """bump version through commitizen"""
    arguments = " --changelog" if changelog else ""
    ctx.run(f"{VENV_PREFIX} cz bump -nr 3 --yes{arguments}", warn=True)
