FROM python:3.11.9-slim

RUN pip install pipx && python -m pipx ensurepath

RUN pipx install nb-cli && \
    pipx install pdm

WORKDIR /opt/iam57-bot

COPY . .

ENV PATH=/root/.local/bin:$PATH

ENV ENVIRONMENT=prod

RUN pdm install

CMD ["nb", "run"]