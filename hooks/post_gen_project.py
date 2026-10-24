import os
import shutil


def remove_pipfile() -> None:
    os.remove("Pipfile")


def remove_invoke_tasks() -> None:
    shutil.rmtree("tasks")


def remove_justfile() -> None:
    os.remove("justfile")


def remove_publish_pypi_github_action() -> None:
    os.remove(".github/workflows/python-publish.yaml")


def remove_docker_file() -> None:
    os.remove("Dockerfile")
    os.remove(".dockerignore")


def remove_cruft_update_action() -> None:
    os.remove(".github/workflows/cruft-update.yaml")


def main() -> None:
    if "{{ cookiecutter.dependency_management_tool }}" != "pipenv":  # noqa: PLR0133
        remove_pipfile()

    task_runner = "{{ cookiecutter.task_runner }}"
    if task_runner != "invoke":
        remove_invoke_tasks()
    if task_runner != "just":
        remove_justfile()

    if "{{ cookiecutter.build_pypi_package }}" == str(False):
        remove_publish_pypi_github_action()

    if "{{ cookiecutter.build_docker_image }}" == str(False):
        remove_docker_file()

    if "{{ cookiecutter.auto_detect_update_from_cruft_template }}" == str(False):
        remove_cruft_update_action()


if __name__ == "__main__":
    main()
