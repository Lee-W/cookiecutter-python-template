import os


def remove_pipfile():
    os.remove("Pipfile")


def main():
    if "{{ cookiecutter.dependency_management_tool }}" != "pipenv":
        remove_pipfile()


if __name__ == "__main__":
    main()
