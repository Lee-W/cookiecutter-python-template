from invoke import task

from tasks.common import VENV_PREFIX


@task
def commit(ctx):
    """Commit through commitizen"""
    ctx.run(f"{VENV_PREFIX} cz commit", pty=True)


@task
def bump(ctx, with_changelog=False):
    """bump version through commitizen"""
    argument = ""
    if with_changelog:
        argument += " --changelog"

    result = ctx.run(f"{VENV_PREFIX} cz bump --yes{argument}", warn=True)
    if result.exited == 3:  # NO_COMMIT_FOUND
        exit(0)
    else:
        exit(result.exited)
