FROM ghcr.io/withlogicco/poetry:1.2.1-python-3.10-buster

COPY pyproject.toml poetry.lock ./
RUN poetry install --no-root

COPY . .

COPY ./entrypoint.sh /
ENTRYPOINT ["sh", "/entrypoint.sh"]