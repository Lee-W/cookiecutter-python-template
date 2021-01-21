# Changelog
## 0.7.0 (2021-01-21)

### Feat

- **readme**: update link to reference to the exact version of this template
- **github-actions**: add pypi-package publishing

## 0.6.3 (2021-01-20)

### Fix

- **github-action**: fix python-check typo

## 0.6.2 (2021-01-18)

### Fix

- **poetry**: fix jinja2 space in pyproject.toml

## 0.6.1 (2020-10-04)

### Fix

- **pytest-config**: fix pyproject.toml typo

## 0.6.0 (2020-09-18)

### Feat

- **github-action**: use  commitizen-tools/commitizen-action
- **style**: update isort >= 5.0.0, pytest >= 6.0.0

### Refactor

- **pre-commit**: update pre-commit repo version
- **github-template**: comment out unnecessary description

## 0.5.0 (2020-08-16)

### Feat

- **readme**: add [PRs Welcome] and [Code style: black] badges

## 0.4.0 (2020-07-24)

### Feat

- **readme**: add template version to readme

## 0.3.0 (2020-07-14)

### Feat

- **style**: use pyproject.toml to config pylint

## 0.2.0 (2020-07-13)

### Feat

- **project-root**: remove pipfile if poetry is used

## 0.1.0 (2020-06-24)

### Refactor

- resolve rebase issues
- remove trailing space
- **git**: setup version for commitizen
- **pre-commit**: initial pre-commit
- **git**: ignore python file

### Feat

- **github**: add issue template and pull_request_template
- split contributing into separate documentation
- **tasks**: add doc task
- **tasks/test**: allow no tests for test task
- **tasks**: add commit-check and enforce bandit when running secuirty heck
- **dependency**: support choosing poetry as management tool
- **project-root**: apply template best practices to root
- **mypy**: add stricter version of mypy config
- **mkdocs**: initial mkdocs setting and remove redundant timestamp cookiecutter variable
- **style**: add black, isort configurations
- **cookiecutter**: add python_version variable
- **cookiecutter**: setup variable for cookiecutter template
- **doc**: init empty CHANGELOG LICENSE and README
- **editor**: init editorconfig for .py and .md
- **style**: add --config=setup.cfg argument to flake8
- **github-action**: add python-check and version-bump actions
- **tasks**: init invoke tasks
- **pre-commit**: init pre-commit config
- **git**: use cookiecutter version to init commitizen version
- init project package and tests
- **git**: ignore python temp files
- **style**: init pylint config
- **style**: init pytest, flake8, mypy config
- **config**: init coverage config
- **git**: add config for commitizen
- **dependency**: init Pipfile

### Fix

- **project-root**: fix bump version task
- fix template style and minor bugs
- **tasks/secure**: fix bandit config
- **project-root**: fix bump-version github action
- **test**: separate pytest config to pytest.ini
- **version**: fix template initial project version to 0.0.1
