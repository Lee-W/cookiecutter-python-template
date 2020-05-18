from invoke import task

from tasks.common import VENV_PREFIX


@task(optional=["clean"])
def build(ctx, clean=True):
    """Build documentation locally"""
    argument = ""
    if clean:
        argument += " --clean"

    ctx.run(f"{VENV_PREFIX} mkdocs build {argument}")


@task(default=True)
def serve(ctx):
    """Run local server"""
    ctx.run(f"{VENV_PREFIX} mkdocs serve")


@task
def deploy(ctx):
    """Deploy to github page"""
    ctx.run(f"{VENV_PREFIX} mkdocs gh-deploy")
