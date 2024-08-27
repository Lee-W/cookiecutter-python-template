from __future__ import annotations

from invoke.collection import Collection
from invoke.context import Context
from invoke.tasks import task


@task
def clean(ctx: Context) -> None:
    """Remove all the tmp files in .gitignore"""
    ctx.run("git clean -Xdf")


build_ns = Collection("build")
build_ns.add_task(clean)  # type: ignore[arg-type]
