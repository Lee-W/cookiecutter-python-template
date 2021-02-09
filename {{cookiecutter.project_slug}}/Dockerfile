FROM python:{PYTHON_VERSION}-slim

ENV PYTHONUNBUFFERED=1
ENV PATH=$PATH:/root/.local/bin
WORKDIR /project

COPY . /project/

RUN python3 -m pip install --upgrade pip && \
    python3 -m pip install --user pipx --no-warn-script-location && \
    python3 -m pipx ensurepath && \
    python3 -m pip install -r requirements.txt