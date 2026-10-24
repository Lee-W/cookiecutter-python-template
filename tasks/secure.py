from invoke.context import Context
from invoke.tasks import task

from tasks.common import VENV_PREFIX


@task
def check_package(ctx: Context) -> None:
    """Check package security"""
    ctx.run(f"{VENV_PREFIX} pip-audit", warn=True)


@task(pre=[check_package], default=True)
def run(ctx: Context) -> None:
    """Check security check through pip-audit"""
