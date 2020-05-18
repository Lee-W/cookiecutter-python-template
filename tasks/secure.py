from invoke import task

from tasks.common import COMMON_TARGETS_AS_STR, VENV_PREFIX


def check_package(ctx):
    """Check package security"""
    ctx.run(f"{VENV_PREFIX} safety")


@task
def bandit(ctx):
    """Check common software vulnerabilities (Use it as reference only)"""
    ctx.run(f"{VENV_PREFIX} bandit -r {COMMON_TARGETS_AS_STR}", pty=True)


@task(pre=[check_package, bandit], default=True)
def run(ctx):
    """Check security check throguh safety and bandit"""
    pass
