from invoke import task

from tasks.common import VENV_PREFIX


@task
def clean(ctx):
    """Remove virtual environement"""
    # TODO
    ctx.run("poetry env remove 3.7", warn=True)


@task
def init(ctx):
    """Install production dependencies"""
    ctx.run("poetry install --no-dev")


@task
def setup_pre_commit_hook(ctx):
    """Setup pre-commit hook to automate check before git commit and git push"""
    ctx.run("git init")
    ctx.run(
        f"{VENV_PREFIX} pre-commit install -t pre-commit & "
        f"{VENV_PREFIX}  pre-commit install -t pre-push & "
        f"{VENV_PREFIX} pre-commit install -t commit-msg"
    )


@task(optional=["without-pre-commit"])
def init_dev(ctx, without_pre_commit=False):
    """Install development dependencies and setup pre-commit hooks"""
    ctx.run("poetry install ")
    if not without_pre_commit:
        setup_pre_commit_hook(ctx)
