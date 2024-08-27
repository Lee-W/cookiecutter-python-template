from __future__ import annotations

from invoke.context import Context
from invoke.tasks import task

from tasks.common import VENV_PREFIX


@task(default=True)
def run(ctx: Context, run_slow_tests: bool = False) -> None:
    """Run test cases"""
    args = "" if run_slow_tests else " -m 'not slow'"
    cmd = f"{VENV_PREFIX} pytest tests{args} -vvv"
    ctx.run(cmd, pty=True)
