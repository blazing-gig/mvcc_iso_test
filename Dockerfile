
FROM python:3.7-slim AS builder

RUN apt-get update

RUN apt-get install -y libpq-dev && apt-get -y install gcc

ENV PYTHONDONTWRITEBYTECODE 1

COPY ./requirements.txt .

RUN python -m venv /opt/venv

ENV PATH="/opt/venv/bin:$PATH"

RUN pip install -r requirements.txt

RUN pip freeze

## multi stage build
FROM python:3.7-alpine

RUN apk add --update --no-cache libpq

WORKDIR /code
COPY --from=builder /opt/venv /opt/venv

COPY . .

