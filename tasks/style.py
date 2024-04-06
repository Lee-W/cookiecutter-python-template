from invoke.tasks import task
from invoke.context import Context

from tasks.common import COMMON_TARGETS_AS_STR, VENV_PREFIX


@task
def ruff(ctx: Context) -> None:
    """Check style through ruff"""
    ctx.run(f"{VENV_PREFIX} ruff {COMMON_TARGETS_AS_STR}")


@task
def mypy(ctx: Context) -> None:
    """Check style through mypy"""
    ctx.run(f"{VENV_PREFIX} mypy")


@task
def black_check(ctx: Context) -> None:
    """Check style through black"""
    ctx.run(f"{VENV_PREFIX} black --check {COMMON_TARGETS_AS_STR}")


@task
def commit_check(ctx: Context, remote: str = "origin") -> None:
    """Check commit message through commitizen"""
    ctx.run(f"{VENV_PREFIX} cz -nr 3 check --rev-range {remote}/master..", warn=True)


@task(pre=[ruff, mypy, black_check, commit_check], default=True)
def run(ctx: Context) -> None:
    """Check style through linter"""
    pass


@task
def black(ctx: Context) -> None:
    ctx.run(f"{VENV_PREFIX} black {COMMON_TARGETS_AS_STR}")


@task(pre=[black, ruff])
def reformat(ctx: Context) -> None:
    """Reformat python files through black and isort"""
    pass
