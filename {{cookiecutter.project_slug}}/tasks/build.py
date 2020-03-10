from invoke import Collection, task


@task
def clean(ctx):
    """Remove all the tmp files in .gitignore"""
    ctx.run("git clean -Xdf")


build_ns = Collection("build")
build_ns.add_task(clean)
