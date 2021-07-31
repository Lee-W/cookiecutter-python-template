from invoke import task

from tasks.common import VENV_PREFIX


@task(default=True)
def run(ctx, run_slow_tests=False):
    """Run test cases"""
    args = ""
    if not run_slow_tests:
        args += " -m 'not slow'"
    cmd = f"{VENV_PREFIX} pytest tests{args}"
    ctx.run(cmd, pty=True)
