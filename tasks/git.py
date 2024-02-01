from invoke import task
from invoke.context import Context


from tasks.common import VENV_PREFIX


@task
def commit(ctx: Context) -> None:
    """Commit through commitizen"""
    ctx.run(f"{VENV_PREFIX} cz commit", pty=True)


@task
def bump(ctx: Context, changelog=False) -> None:
    """bump version through commitizen"""
    argument = ""
    if changelog:
        argument += " --changelog"

    ctx.run(f"{VENV_PREFIX} cz bump -nr 3 --yes{argument}", warn=True)
