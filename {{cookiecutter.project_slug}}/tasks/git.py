from invoke import task

from tasks.common import VENV_PREFIX


@task
def commit(ctx):
    """Commit through commitizen"""
    ctx.run(f"{VENV_PREFIX} cz commit", pty=True)


@task
def bump(ctx):
    """bump version through commitizen"""
    ctx.run(f"{VENV_PREFIX} cz bump --yes", warn=True)
