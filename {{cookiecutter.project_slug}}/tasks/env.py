from invoke import task


@task
def clean(ctx):
    """Remove virtual environement"""
    ctx.run("pipenv --rm", warn=True)


@task
def init(ctx):
    """Install production dependencies"""
    ctx.run("pipenv install --deploy")


@task
def setup_pre_commit_hook(ctx):
    """Setup pre-commit hook to automate check before git commit and git push"""
    ctx.run("git init")
    ctx.run(
        "pipenv run pre-commit install -t pre-commit & "
        "pipenv run pre-commit install -t pre-push & "
        "pipenv run pre-commit install -t commit-msg"
    )


@task(post=[setup_pre_commit_hook])
def init_dev(ctx):
    """Install development dependencies and setup pre-commit hooks"""
    ctx.run("pipenv install --dev")
