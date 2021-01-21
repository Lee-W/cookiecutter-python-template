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


build_ns = Collection("build")
build_ns.add_task(clean)
{% if "{{ cookiecutter.build_pypi_package }}" != "n" -%}
build_ns.add_task(dist)
{%- endif %}
