from invoke.context import Context
from invoke.tasks import task

from tasks.common import VENV_PREFIX


@task(default=True)
def run(ctx: Context) -> None:
    """Check package security through pip-audit (code security is covered by ruff's "S" rules)"""
    ctx.run(f"{VENV_PREFIX} pip-audit", warn=True)
