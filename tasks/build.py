from invoke import Collection, task
from invoke.context import Context


@task
def clean(ctx: Context) -> None:
    """Remove all the tmp files in .gitignore"""
    ctx.run("git clean -Xdf")


build_ns = Collection("build")
build_ns.add_task(clean)  # type: ignore[arg-type]
