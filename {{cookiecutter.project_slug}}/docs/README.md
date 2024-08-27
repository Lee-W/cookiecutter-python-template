[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)
[![Conventional Commits](https://img.shields.io/badge/Conventional%20Commits-1.0.0-yellow.svg?style=flat-square)](https://conventionalcommits.org)
[![Github Actions]({{ cookiecutter.github_url }}/actions/workflows/python-check.yaml/badge.svg)]({{ cookiecutter.github_url }}/actions/workflows/python-check.yaml)
{% if cookiecutter.build_pypi_package != "n" %}
[![PyPI Package latest release](https://img.shields.io/pypi/v/{{ cookiecutter.project_slug }}.svg?style=flat-square)](https://pypi.org/project/{{ cookiecutter.project_slug }}/)
[![PyPI Package download count (per month)](https://img.shields.io/pypi/dm/{{ cookiecutter.project_slug }}?style=flat-square)](https://pypi.org/project/{{ cookiecutter.project_slug }}/)
[![Supported versions](https://img.shields.io/pypi/pyversions/{{ cookiecutter.project_slug }}.svg?style=flat-square)](https://pypi.org/project/{{ cookiecutter.project_slug }}/)
{% endif %}

# {{ cookiecutter.project_slug }}

{{ cookiecutter.project_description }}

## Getting Started

### Prerequisites
* [Python](https://www.python.org/downloads/)

## Usage

## Contributing
See [Contributing](contributing.md)

## Authors
{{ cookiecutter.author_name }} <{{ cookiecutter.author_email }}>

Created from [Lee-W/cookiecutter-python-template](https://github.com/Lee-W/cookiecutter-python-template/tree/{{ cookiecutter._template_version }}) version {{ cookiecutter._template_version }}
