FROM python:{{ cookiecutter.python_version }}-slim-stretch

ENV PYTHONUNBUFFERED=1
ENV PYTHONFAULTHANDLER=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV USERNAME = {{ cookiecutter.github_username.lower().replace(' ', '_').replace('-', '_') }}
ENV PATH=$PATH:/home/$USERNAME/.local/bin

RUN useradd --create-home $USERNAME
USER $USERNAME
WORKDIR /home/$USERNAME

COPY . /home/$USERNAME/

RUN python3 -m pip install --upgrade pip && \
    python3 -m pip install --no-cache-dir -r requirements.txt
