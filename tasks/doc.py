from __future__ import annotations

from invoke.context import Context
from invoke.tasks import task

from tasks.common import VENV_PREFIX


@task(optional=["clean"])
def build(ctx: Context, clean: bool = True) -> None:
    """Build documentation locally"""
    arguments = " --clean" if clean else ""
    ctx.run(f"{VENV_PREFIX} mkdocs build {arguments}")


@task(default=True)
def serve(ctx: Context) -> None:
    """Run local server"""
    ctx.run(f"{VENV_PREFIX} mkdocs serve")


@task
def deploy(ctx: Context) -> None:
    """Deploy to github page"""
    ctx.run(f"{VENV_PREFIX} mkdocs gh-deploy")
