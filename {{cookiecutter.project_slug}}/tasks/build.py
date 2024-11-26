from __future__ import annotations

from invoke.collection import Collection
from invoke.context import Context
from invoke.tasks import task
{% if cookiecutter.dependency_management_tool == 'pipenv' -%}
from tasks.common import VENV_PREFIX
{% endif %}

@task
def clean(ctx: Context) -> None:
    """Remove all the tmp files in .gitignore"""
    ctx.run("git clean -Xdf")


{% if "{{ cookiecutter.build_pypi_package }}" -%}
@task
def dist(ctx: Context) -> None:
    """Build distribution"""
    {% if cookiecutter.dependency_management_tool == "uv" -%}
    ctx.run("uv build")
    {%- elif cookiecutter.dependency_management_tool == "poetry" -%}
    ctx.run("poetry build")
    {%- elif cookiecutter.dependency_management_tool == "pipenv" -%}
    ctx.run(f"{VENV_PREFIX} python setup.py sdist bdist_wheel")
    {%- endif %}
{%- endif %}


{% if "{{ cookiecutter.build_docker_image }}" -%}
@task
def docker(ctx: Context) -> None:
    """Build docker image"""
    {% if cookiecutter.dependency_management_tool == "uv" -%}
    ctx.run("uv lock")
    {%- elif cookiecutter.dependency_management_tool == "poetry" -%}
    ctx.run("poetry export -f requirements.txt -o requirements.txt")
    {%- elif cookiecutter.dependency_management_tool == "pipenv" -%}
    ctx.run("pipenv lock && pipenv requirements")
    {%- endif %}
    user_name = "{{ cookiecutter.github_username.lower().replace(' ', '_').replace('-', '_') }}"
    proj_name = "{{ cookiecutter.project_name.lower().replace(' ', '_').replace('-', '_') }}"
    repo_name = f"{user_name}/{proj_name}"
    ctx.run(f"docker build -t {repo_name}:latest .")
{%- endif %}


build_ns = Collection("build")
build_ns.add_task(clean)  # type: ignore[arg-type]
{% if "{{ cookiecutter.build_pypi_package }}" -%}
build_ns.add_task(dist)  # type: ignore[arg-type]
{%- endif %}
{% if "{{ cookiecutter.build_docker_image }}" -%}
build_ns.add_task(docker)  # type: ignore[arg-type]
{%- endif %}
