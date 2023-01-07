[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)
[![Conventional Commits](https://img.shields.io/badge/Conventional%20Commits-1.0.0-yellow.svg?style=flat-square)](https://conventionalcommits.org)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Github Actions](https://github.com/Lee-W/cookiecutter-python-template/actions/workflows/pushed.yaml/badge.svg)](https://github.com/Lee-W/cookiecutter-python-template/actions/workflows/pushed.yaml)
# Cookiecutter Python Template

## Features

* [pipenv](https://pipenv.pypa.io/en/latest/) or [poetry](https://python-poetry.org/): dependency and virtual environment management
* Coding style
    * [flake8](https://flake8.pycqa.org/en/latest/) and [pylint](https://pylint.org/) (optional): check style, programming errors and complexity
    * [mypy](http://mypy-lang.org/): check static type
    * [black](https://github.com/psf/black): auto format your code
    * [isort](https://pycqa.github.io/isort/): auto sort your package importing
* Test thought [pytest](https://docs.pytest.org/en/) with the following supports
    * [pytest-cov](https://github.com/pytest-dev/pytest-cov): generate test coverage repo
    * [pytest-mock](https://github.com/pytest-dev/pytest-mock/): mocking
    * [pytest-xdist](https://github.com/pytest-dev/pytest-xdist): distributed testing
* [commitizen](https://commitizen-tools.github.io/commitizen/):
    * regulate git commit convention
    * bump project version
    * generate changelog automatically
* [mkdocs](https://www.mkdocs.org/): generate documentation
* [invoke](http://www.pyinvoke.org/): organize the tools above
* [pre-commit](https://pre-commit.com/): git-hook to run the above tools automatically
* GitHub
    * [GitHub Actions](https://docs.github.com/en/actions) workflows for checking style, testing, publishing package to PyPI and pushing documentation to GitHub pages
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

* Add required secrets to your GitHub repository secrets
    * `PERSONAL_ACCESS_TOKEN`: GitHub personal access token
        * Refer to [Creating a personal access token](https://docs.github.com/en/github/authenticating-to-github/keeping-your-account-and-data-secure/creating-a-personal-access-token) to generate one
    * `pypi_password`: PyPI API token
        * required only if you set "build_pypi_package" to "y" during project creation
        * Refer to [How can I use API tokens to authenticate with PyPI?](https://pypi.org/help/#apitoken) to generate one. Note that username `__token__` has been setup in the project

## Authors
[Lee-W](https://github.com/Lee-W)
