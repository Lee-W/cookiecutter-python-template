import os


def remove_pipfile() -> None:
    os.remove("Pipfile")


def remove_publish_pypi_github_action() -> None:
    os.remove(".github/workflows/python-publish.yaml")


def remove_docker_file() -> None:
    os.remove("Dockerfile")
    os.remove(".dockerignore")


def main() -> None:
    if "{{ cookiecutter.dependency_management_tool }}" != "pipenv":
        remove_pipfile()

    if "{{ cookiecutter.build_pypi_package }}" == "n":
        remove_publish_pypi_github_action()

    if "{{ cookiecutter.build_docker_image }}" == "n":
        remove_docker_file()


if __name__ == "__main__":
    main()
