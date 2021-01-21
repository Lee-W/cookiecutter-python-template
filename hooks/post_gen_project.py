import os


def remove_pipfile():
    os.remove("Pipfile")


def remove_publish_pypi_github_action():
    os.remove(".github/workflows/python-publish.yaml")


def main():
    if "{{ cookiecutter.dependency_management_tool }}" != "pipenv":
        remove_pipfile()

    if "{{ cookiecutter.build_pypi_package }}" == "n":
        remove_publish_pypi_github_action()


if __name__ == "__main__":
    main()
