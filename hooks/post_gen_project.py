import os


def remove_pipfile():
    os.remove("Pipfile")


def remove_publish_pypi_github_action():
    os.remove(".github/workflows/python-publish.yaml")


def remove_docker_file():
    os.remove("Dockerfile")


def main():
    if "{{ cookiecutter.dependency_management_tool }}" != "pipenv":
        remove_pipfile()

    if "{{ cookiecutter.build_pypi_package }}" == "n":
        remove_publish_pypi_github_action()

    if "{{ cookiecutter.build_docker_image }}" == "n":
        remove_docker_file()


if __name__ == "__main__":
    main()
