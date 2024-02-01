from invoke import task
from invoke.context import Context

from tasks.common import VENV_PREFIX


@task(default=True)
def run(ctx: Context, run_slow_tests=False) -> None:
    """Run test cases"""
    args = ""
    if not run_slow_tests:
        args += " -m 'not slow'"
    cmd = f"{VENV_PREFIX} pytest tests{args}"
    ctx.run(cmd, pty=True)
