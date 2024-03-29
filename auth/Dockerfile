FROM python:3.11.3-slim-buster as build

WORKDIR /opt/auth

COPY ./requirements.txt .

RUN apt update \
    && apt install -y gcc libpq-dev \
    && python -m venv venv \
    && venv/bin/pip install --no-cache-dir --upgrade pip \
    && venv/bin/pip install --no-cache-dir -r requirements.txt

FROM python:3.11.3-slim-buster

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PATH="/opt/auth/venv/bin:${PATH}" \
    PYTHONPATH="/opt/auth/src:${PYTHONPATH}"

ARG APP=/opt/auth
ARG USER=web

WORKDIR ${APP}

RUN apt update \
    && apt install -y --no-install-recommends \
      libpq-dev \
      netcat \
    && rm -rf /var/lib/apt/lists/* \
    && groupadd -r ${USER} \
    && useradd -d ${APP} -r -g ${USER} ${USER}

COPY --chown=${USER}:${USER} --from=build ${APP}/venv ./venv
COPY --chown=${USER}:${USER} . .

RUN chmod +x ${APP}/entrypoint.sh

USER ${USER}

ENTRYPOINT ["/opt/auth/entrypoint.sh"]
