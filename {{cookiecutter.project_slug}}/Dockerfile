{% if cookiecutter.dependency_management_tool == "uv" -%}
FROM ghcr.io/astral-sh/uv:python{{ cookiecutter.python_version }}-bookworm-slim AS builder
{%- else -%}
FROM python:{{ cookiecutter.python_version }}-slim-bookworm AS builder
{%- endif %}

WORKDIR /app
COPY . /app

{% if cookiecutter.dependency_management_tool == "uv" -%}
ENV UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy

RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --frozen --no-install-project --no-dev

RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-dev
{%- else -%}
ENV PYTHONUNBUFFERED=1 \
    PYTHONFAULTHANDLER=1 \
    PYTHONDONTWRITEBYTECODE=1

RUN python3 -m venv .venv

ENV PATH="/app/.venv/bin:$PATH"

RUN python3 -m pip install --no-cache-dir --upgrade pip && \
    python3 -m pip install --no-cache-dir -r requirements.txt
{%- endif %}


FROM python:{{ cookiecutter.python_version }}-slim-bookworm

ARG USERNAME={{ cookiecutter.github_username.lower().replace(' ', '_').replace('-', '_') }}

RUN useradd -m $USERNAME
USER $USERNAME
WORKDIR /app

COPY --from=builder --chown=$USERNAME:$USERNAME /app /app

ENV PATH="/app/.venv/bin:$PATH"
