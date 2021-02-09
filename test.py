import os


def generate_docker_file(yes, python_version):
    if yes:
        with open("Dockerfile_general", "r") as rf:
            docker_file_content = rf.read().format(PYTHON_VERSION=python_version)
            rf.close()
        with open("Dockerfile", "w") as wf:
            wf.write(docker_file_content)
            wf.close()
    # os.remove("Dockerfile_general")


generate_docker_file(True, "3.8")
