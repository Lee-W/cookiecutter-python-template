FROM python:{{ cookiecutter.python_version }}-slim-stretch

ARG USERNAME={{ cookiecutter.github_username.lower().replace(' ', '_').replace('-', '_') }}

ENV PYTHONUNBUFFERED=1 \
    PYTHONFAULTHANDLER=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PATH=$PATH:/home/$USERNAME/.local/bin

RUN useradd --create-home $USERNAME
USER $USERNAME
WORKDIR /home/$USERNAME

COPY . /home/$USERNAME/

RUN python3 -m pip install --upgrade pip==24.0 && \
    python3 -m pip install --no-cache-dir -r requirements.txt
