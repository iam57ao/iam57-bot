FROM python:3.11.9-bullseye

RUN pip install pipx && python -m pipx ensurepath

RUN pipx install nb-cli && \
    pipx install pdm

WORKDIR /opt/iam57-bot

COPY ../ .

ENV PATH=/root/.local/bin:$PATH