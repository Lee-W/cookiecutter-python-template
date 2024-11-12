[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)
[![Conventional Commits](https://img.shields.io/badge/Conventional%20Commits-1.0.0-yellow.svg?style=flat-square)](https://conventionalcommits.org)
[![Github Actions](https://github.com/Lee-W/cookiecutter-python-template/actions/workflows/pushed.yaml/badge.svg)](https://github.com/Lee-W/cookiecutter-python-template/actions/workflows/pushed.yaml)

# Cookiecutter Python Template

## Features

* [pipenv](https://pipenv.pypa.io/en/latest/) or [poetry](https://python-poetry.org/): dependency and virtual environment management
* Coding style
    * [ruff](https://github.com/astral-sh/ruff): check coding style and format it
    * [mypy](http://mypy-lang.org/): check static typing
* Test thought [pytest](https://docs.pytest.org/en/) with the following plugins
    * [pytest-cov](https://github.com/pytest-dev/pytest-cov): generate test coverage repo
    * [pytest-mock](https://github.com/pytest-dev/pytest-mock/): mocking
* [commitizen](https://commitizen-tools.github.io/commitizen/):
    * regulate git commit convention
    * bump project version
    * generate changelog automatically
* Security check through
    * [bandit](https://github.com/PyCQA/bandit)
    * [pip-audit](https://pypi.org/project/pip-audit/)
* [mkdocs](https://www.mkdocs.org/): generate documentation
* [pre-commit](https://pre-commit.com/): git-hook to run the above tools automatically
* [invoke](http://www.pyinvoke.org/): organize the tools above (like Makefile in PYthon)
* CI/CD
    * [GitHub Actions](https://docs.github.com/en/actions) workflows for
        * checking coding style
        * testing
        * publishing package to PyPI
        * pushing documentation to GitHub pages
    * GitHub issue templates, pull request template
* General Python project Dockerfile
* Consolidate most of the tool configurations in `pyproject.toml`

## Getting Started

### Prerequisites

* [Python](https://www.python.org/downloads/)
* [cruft](https://cruft.github.io/cruft/)

## Usage

```sh
cruft create https://github.com/Lee-W/cookiecutter-python-template
```

### Setup secrets for GitHub Actions
* Required GitHub repository secrets
    * `PERSONAL_ACCESS_TOKEN`: GitHub personal access token used to bump project version automatically
        * Refer to [Creating a personal access token](https://docs.github.com/en/github/authenticating-to-github/keeping-your-account-and-data-secure/creating-a-personal-access-token) to generate one
    * (optional) `pypi_password`: PyPI API token
        * required only if you set "build_pypi_package" to "y" during project creation
        * Refer to [How can I use API tokens to authenticate with PyPI?](https://pypi.org/help/#apitoken) to generate one. Note that username `__token__` has been setup in the project

## Authors

[Lee-W](https://github.com/Lee-W)
