FROM python:{{ cookiecutter.python_version }}-slim

ENV PYTHONUNBUFFERED=1
ENV PYTHONFAULTHANDLER=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV PATH=$PATH:/root/.local/bin

RUN useradd --create-home appuser
USER appuser
WORKDIR /home/appuser

COPY . /home/appuser/

RUN python3 -m pip install --upgrade pip && \
    python3 -m pip install --no-cache-dir -r requirements.txt
