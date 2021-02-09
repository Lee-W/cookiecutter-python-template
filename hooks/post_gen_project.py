import os


def remove_pipfile():
    os.remove("Pipfile")


def remove_publish_pypi_github_action():
    os.remove(".github/workflows/python-publish.yaml")


def generate_docker_file(yes, python_version):
    if not yes:
        os.remove("Dockerfile_template")
        return
    with open("Dockerfile_template", "r") as rf:
        docker_file_content = rf.read().format(PYTHON_VERSION=python_version)
        rf.close()
    with open("Dockerfile", "w") as wf:
        wf.write(docker_file_content)
        wf.close()
    os.remove("Dockerfile_template")


def main():
    if "{{ cookiecutter.dependency_management_tool }}" != "pipenv":
        remove_pipfile()

    if "{{ cookiecutter.build_pypi_package }}" == "n":
        remove_publish_pypi_github_action()

    generate_docker_file(
        "{{ cookiecutter.add_general_dockerfile }}" != "n",
        "{{ cookiecutter.python_version }}",
    )


if __name__ == "__main__":
    main()
