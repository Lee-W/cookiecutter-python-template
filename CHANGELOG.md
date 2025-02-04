# Changelog
## 3.0.0 (2025-01-19)

### Feat

- **poetry**: update to poetry >= 2.0 spec

## 2.0.0 (2024-12-04)

### Feat

- **docker**: add uv support
- migrate pre-commit config
- **dependency_management_tool**: add uv support
- **poetry**: add package-mode support
- **github-actions**: make cruft-update python version configurable
- group Pipfile, pyproject.toml dependencies
- **pre-commit**: migrate pre-commit config
- **cookiecutter**: make python version a choice
- **cookiecutter**: Use boolean variable in cookiecutter.json
- **pre-commit**: add markdownlint and spellcheck
- **spellcheck**: initialize spelling worklist

### Fix

- **Dockerfile**: fix hadolint warning
- **pyproject.toml**: fix format

### Refactor

- extract package version as variable and manage them in cookiecutter.json
- **github-actions**: extract setup-version and manage it through _setup_uv_version variable
- simplify unnecessay cookiecutter.dependency_management_tool comparing
- **github-actions**: unify actions/setup-python version
- **github-actions**: unify actions/checkout version

## 1.11.0 (2024-08-28)

### Feat

- update poetry dependencies syntax with latest group syntax
- change default python version to 3.9
- **github-acitons**: change dependabot check to weekly
- remove black and update project dev dependencies

### Fix

- **github-actions**: replace deprecated @master pypa/gh-action-pypi-publish with @release/v1
- **github-actions**: fix cruft-update action render error

### Refactor

- **tasks**: simplify arguments

## 1.10.1 (2024-05-28)

### Fix

- **pre-commit**: fix pre-commit-config missing venv

## 1.10.0 (2024-04-20)

### Feat

- upgrade ruff related config due to ruff upgrade

## 1.9.3 (2024-04-06)

### Fix

- **tasks**: fix missing hook-stage in run-pre-commit-hooks task

## 1.9.2 (2024-04-06)

### Fix

- **github-actions**: skip no-commit-to-branch in CI which causes false negative when bumping version

## 1.9.1 (2024-04-06)

### Fix

- **tasks**: fix import error

## 1.9.0 (2024-04-06)

### Feat

- **github-actions**: add github-actions to detect cruft template update
- **dockerfile**: pin pip version
- **deps**: upgrade pre-commit to >= 3.0.0 for actionlint
- **github-actions**: run pre-commit hooks on github action

## 1.8.1 (2024-02-17)

### Fix

- **workflows**: change actions version

## 1.8.0 (2024-02-01)

### Feat

- **pre-commit**: add actionlint
- **dependency**: upgrade dev tools versions and remove pytest-xdist, hypothesis which might not be needed in every project
- **github-actions**: pin action versions

## 1.7.0 (2023-06-24)

### Feat

- upgrade invoke version to 2.1.3
- upgrade mypy to >= 1.4

### Fix

- **secure**: fix doc string typo

## 1.6.0 (2023-06-17)

### Feat

- add dependabot setup

## 1.5.0 (2023-06-17)

### Feat

- introduce ruff and pre-commit hooks

## 1.4.0 (2022-11-24)

### Feat

- replace safety with pip-audit
- **poetry**: pin pytest to >= 7.2.0 for resolving the security issue caused by "py"

### Fix

- **pre-commit**: remove outdated cookiecutter.add_general_dockerfile and replace it with build_docker_image option
- fix various minor errors

## 1.3.0 (2022-09-17)

### Feat

- **project-root**: upgrade project-root python version to 3.10 and upgrade deps

### Fix

- **github-actions**: set persist-credentials to false for check-out actions
- **github-actions**: use personal access token to replace github token
- **tasks/style**: fix commit check command

## 1.2.1 (2022-09-17)

### Fix

- **tasks/build**: fix missing import when pipenv is used

## 1.2.0 (2022-09-17)

### Feat

- **github-actions**: replace md issue template with yaml

### Fix

- **hooks**: remove .dockerfile if Docker setup is not chosen

## 1.1.2 (2021-10-09)

### Fix

- **mypy-config**: use module instead files to specify overrides

## 1.1.1 (2021-08-08)

### Fix

- **github-actions**: fix missing @ for setup python step

## 1.1.0 (2021-08-05)

### Fix

- **docs**: fix contributing page missing space

### Feat

- **gitignore**: update gitignore content

### Refactor

- **github-actions**: remove redundant checkout

## 1.0.0 (2021-07-31)

### Fix

- **docker**: rename add_general_dockerfile as build_docker_image and move hadolint to template from project root
- **license**: fix end of line

### Feat

- **tasks/env**: add autoupdate to pre-commit
- **pre-commit**: add check-case-conflict, check-merge-conflict, no-commit-to-branch and change style format stage to commit
- **github-actions**: add workflow-dispatch to python-check
- **mypy**: migrate configuration to pyproject.toml

## 0.9.1 (2021-07-05)

### Fix

- **tasks**: fix safety command

## 0.9.0 (2021-05-07)

### Fix

- **github-actions**: fix bump-version action
- **github-actions**: fix gh-pages publishing action
- **pre-commit**: fix commitizen version
- **cookiecutter**: remove .mypy_cache when generating template
- **github-actions**: remove unused tag configuration in commitizen github actions
- **mypy**: remove empty line between mypy config

### Feat

- **pyproject.toml**: add project metadata if poetry is used
- support default branch name choices

## 0.8.0 (2021-02-10)

### Feat

- **dockerize**: improve docker file
- **dockerize**: improve docker file
- **dockerize**: rewrite dockerfile template
- **dockerize**: patch post hook
- **dockerize**: add general docker file

### Fix

- **dockerize**: fix repo name
- **dockerize**: improve docker build process
- **dockerize**: rm manifest
- **dockerize**: patch post hook
- **dockerize**: patch post hook
- **dockerize**: update manifest
- **dockerize**: keep dockerfile
- **dockerize**: move manifest
- **dockerize**: add manifest for non-python file
- **dockerize**: test do not remove dockerfile

## 0.7.3 (2021-01-28)

### Fix

- **cookiecutter.json**: use https by default

## 0.7.2 (2021-01-26)

### Fix

- **license**: use correct BSD license name

## 0.7.1 (2021-01-23)

### Fix

- **tasks**: run commands for installing pre-commit hooks sequentially

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
- **tasks**: add commit-check and enforce bandit when running security heck
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
