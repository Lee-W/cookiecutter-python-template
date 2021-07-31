from invoke import Collection, task


@task
def clean(ctx):
    """Remove all the tmp files in .gitignore"""
    ctx.run("git clean -Xdf")


{% if "{{ cookiecutter.build_pypi_package }}" != "n" -%}
@task
def dist(ctx):
    """Build distribution"""
    {% if cookiecutter.dependency_management_tool == 'pipenv' -%}
    ctx.run(f"{VENV_PREFIX} python setup.py sdist bdist_wheel")
    {%- elif cookiecutter.dependency_management_tool == 'poetry' -%}
    ctx.run("poetry build")
    {%- endif %}
{%- endif %}


{% if "{{ cookiecutter.build_docker_image }}" != "n" -%}
@task
def docker(ctx):
    """Build docker image"""
    {% if cookiecutter.dependency_management_tool == 'pipenv' -%}
    ctx.run("pipenv lock --keep-outdated --requirements > requirements.txt")
    {%- elif cookiecutter.dependency_management_tool == 'poetry' -%}
    ctx.run("poetry export -f requirements.txt -o requirements.txt")
    {%- endif %}
    user_name = "{{ cookiecutter.github_username.lower().replace(' ', '_').replace('-', '_') }}"
    proj_name = "{{ cookiecutter.project_name.lower().replace(' ', '_').replace('-', '_') }}"
    repo_name = f"{user_name}/{proj_name}"
    ctx.run(f"docker build -t {repo_name}:latest .")
{%- endif %}


build_ns = Collection("build")
build_ns.add_task(clean)
{% if "{{ cookiecutter.build_pypi_package }}" != "n" -%}
build_ns.add_task(dist)
{%- endif %}
{% if "{{ cookiecutter.build_docker_image }}" != "n" -%}
build_ns.add_task(docker)
{%- endif %}
