from invoke import task

from tasks.common import COMMON_TARGETS_AS_STR, VENV_PREFIX


@task
def ruff(ctx):
    """Check style through ruff"""
    ctx.run(f"{VENV_PREFIX} ruff {COMMON_TARGETS_AS_STR}")


@task
def mypy(ctx):
    """Check style through mypy"""
    ctx.run(f"{VENV_PREFIX} mypy")


@task
def black_check(ctx):
    """Check style through black"""
    ctx.run(f"{VENV_PREFIX} black --check {COMMON_TARGETS_AS_STR}")


@task
def commit_check(ctx, remote="origin"):
    """Check commit message through commitizen"""
    ctx.run(
        f"{VENV_PREFIX} cz -nr 3 check --rev-range {remote}/{{ cookiecutter.default_branch }}..",
        warn=True
    )


@task(pre=[ruff, mypy, black_check, commit_check], default=True)
def run(ctx):
    """Check style through linter (Note that pylint is not included)"""
    pass


@task
def black(ctx):
    ctx.run(f"{VENV_PREFIX} black {COMMON_TARGETS_AS_STR}")


@task(pre=[ruff, black])
def reformat(ctx):
    """Reformat python files through black and isort"""
    pass
