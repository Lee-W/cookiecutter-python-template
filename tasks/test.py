from invoke import task

from tasks.common import VENV_PREFIX


@task(default=True)
def run(ctx):
    """Run test cases"""
    ctx.run(f"{VENV_PREFIX} pytest tests", pty=True)
