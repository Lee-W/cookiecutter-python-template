from __future__ import annotations

from invoke.context import Context
from invoke.tasks import task

from tasks.common import VENV_PREFIX


@task
def check_package(ctx: Context) -> None:
    """Check package security"""
    ctx.run(f"{VENV_PREFIX} pip-audit", warn=True)


@task
def bandit(ctx: Context) -> None:
    """Check common software vulnerabilities (Use it as reference only)"""
    ctx.run(f"{VENV_PREFIX} bandit -r -iii -lll --ini .bandit", pty=True)


@task(pre=[check_package, bandit], default=True)
def run(ctx: Context) -> None:
    """Check security check through pip-audit and bandit"""
    pass
