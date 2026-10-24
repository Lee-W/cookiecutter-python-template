{#- Single place that decides how the docs invoke the project task runner -#}
{%- set tool = cookiecutter.dependency_management_tool -%}
{%- if cookiecutter.task_runner == "invoke" -%}
{%- set run_task = tool ~ " run inv" -%}
{%- set dot = "." -%}
{%- elif cookiecutter.task_runner == "poethepoet" -%}
{%- set run_task = tool ~ " run poe" -%}
{%- set dot = "-" -%}
{%- else -%}
{%- set run_task = "just" -%}
{%- set dot = "-" -%}
{%- endif -%}
### Step 1. Fork this repository to your GitHub

### Step 2. Clone the repository from your GitHub

```sh
git clone https://github.com/[YOUR GITHUB ACCOUNT]/{{ cookiecutter.project_slug }}.git
```

### Step 3. Add this repository to the remote in your local repository

```sh
git remote add upstream "{{ cookiecutter.github_url }}"
```

You can pull the latest code in {{ cookiecutter.default_branch }} branch through `git pull upstream {{ cookiecutter.default_branch }}` afterward.

### Step 4. Check out a branch for your new feature

```sh
git checkout -b [YOUR FEATURE]
```

### Step 5. Install prerequisite

```sh
{% if tool == "uv" -%}
python -m pip install uv
{%- if cookiecutter.task_runner == "just" %}
uv tool install rust-just  # or `brew install just`
{%- endif %}
{%- else -%}
python -m pip install pipx
python -m pipx install {{ tool }} {{ {"invoke": "invoke", "poethepoet": "poethepoet", "just": "rust-just"}[cookiecutter.task_runner] }}
python -m pipx ensurepath
{%- endif %}
```

{% if tool == "uv" -%}
* [uv tool](https://docs.astral.sh/uv/guides/tools/): for python tool management
{%- else -%}
* [pipx](https://github.com/pypa/pipx): for python tool management
{%- endif %}
{%- if tool == 'pipenv' %}
* [pipenv](https://github.com/pypa/pipenv): for dependency management
{%- elif tool == 'poetry' %}
* [poetry](https://python-poetry.org/): for dependency management
{%- endif %}
{% if cookiecutter.task_runner == "invoke" -%}
* [invoke](https://github.com/pyinvoke/invoke): for task management
{%- elif cookiecutter.task_runner == "poethepoet" -%}
* [poethepoet](https://poethepoet.natn.io/): for task management
{%- else -%}
* [just](https://github.com/casey/just): for task management (installed from the `rust-just` package, which ships the `just` executable)
{%- endif %}

### Step 6. Create your local Python virtual environment and install dependencies

```sh
{{ run_task }} env{{ dot }}init-dev
```

### Step 7. Work on your new feature
Note that this project follows [conventional-commit](https://www.conventionalcommits.org/en/v1.0.0/) and bumps version based on it. Use the following command to commit your changes.

```sh
{{ run_task }} git{{ dot }}commit
```

### Step 8. Run test cases
Make sure all test cases pass.

```sh
{{ run_task }} test
```

### Step 9. Run test coverage
Check the test coverage and see where you can add test cases.

```sh
{{ run_task }} test{{ dot }}cov
```

### Step 10. Reformat source code

Format your code through `ruff`.

```sh
{{ run_task }} style{{ dot }}format
```

### Step 11. Run style check
Make sure your coding style passes all enforced linters.

```sh
{{ run_task }} style
```

### Step 12. Run security check

Ensure the packages installed have no known vulnerabilities (`pip-audit`). Code-level security checks are part of `style` through the ruff `S` rules.

```sh
{{ run_task }} secure
```

### Step 13. Create a Pull Request and celebrate 🎉
