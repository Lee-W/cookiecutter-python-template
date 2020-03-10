from invoke import task

from tasks.common import COMMON_TARGETS_AS_STR, PIPENV_PREFIX


@task(default=True)
def check_package(ctx):
    """Check package security"""
    ctx.run("pipenv check")


@task
def bandit(ctx):
    """Check common software vulnerabilities (Use it as reference only)"""
    ctx.run(f"{PIPENV_PREFIX} bandit -r {COMMON_TARGETS_AS_STR}", pty=True)
