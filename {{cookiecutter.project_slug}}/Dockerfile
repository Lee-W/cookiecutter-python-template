{% if cookiecutter.dependency_management_tool == "uv" -%}
FROM ghcr.io/astral-sh/uv:python{{ cookiecutter.python_version }}-trixie-slim AS builder
{%- else -%}
FROM python:{{ cookiecutter.python_version }}-slim-trixie AS builder
{%- endif %}

WORKDIR /app

{% if cookiecutter.dependency_management_tool == "uv" -%}
ENV UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy

# Install dependencies first so this layer stays cached until the lock file changes
RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --frozen --no-install-project --no-dev

COPY . /app

RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-dev
{%- elif cookiecutter.dependency_management_tool == "poetry" -%}
ENV PYTHONUNBUFFERED=1 \
    PYTHONFAULTHANDLER=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=true

RUN python3 -m pip install --no-cache-dir poetry=={{ cookiecutter._package_versions.poetry }}

# Install dependencies first so this layer stays cached until the lock file changes
# (all PEP 735 dependency groups are installed by default in poetry, so exclude them explicitly;
# poetry validates the license and readme files declared in pyproject.toml even with --no-root)
COPY pyproject.toml poetry.lock LICENSE ./
COPY docs/README.md docs/README.md
RUN poetry install --without dev,test,style,security,git,doc --no-root

COPY . /app

RUN poetry install --without dev,test,style,security,git,doc
{%- else -%}
ENV PYTHONUNBUFFERED=1 \
    PYTHONFAULTHANDLER=1 \
    PYTHONDONTWRITEBYTECODE=1

RUN python3 -m venv .venv

ENV PATH="/app/.venv/bin:$PATH"

# Install dependencies first so this layer stays cached until requirements.txt changes
COPY requirements.txt ./
RUN python3 -m pip install --no-cache-dir -r requirements.txt

COPY . /app
{%- endif %}


FROM python:{{ cookiecutter.python_version }}-slim-trixie

ARG APP_USER={{ cookiecutter.github_username.lower().replace(' ', '_').replace('-', '_') }}

RUN useradd -m $APP_USER
USER $APP_USER
WORKDIR /app

COPY --from=builder --chown=$APP_USER:$APP_USER /app /app

ENV PATH="/app/.venv/bin:$PATH"
