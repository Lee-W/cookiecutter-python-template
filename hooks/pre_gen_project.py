import shutil
from pathlib import Path


def remove_mypy_cache():
    # .mypy_cache frequently causes jinja2 template error
    for path in Path(".").glob("**/.mypy_cache"):
        shutil.rmtree(path)


def main():
    remove_mypy_cache()


if __name__ == "__main__":
    main()
