FROM python:3

# python envs
ENV PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=10 \
    DEBUG=False \
    RDS_DB_NAME=postgres \
    RDS_USERNAME=postgres \
    RDS_PASSWORD=postgrespassword \
    RDS_HOSTNAME=db \
    RDS_PORT=5432 \
    SECRET_KEY=super-secret-key

COPY ./requirements.txt /

RUN pip install -r /requirements.txt

COPY . /app

# collect static files
WORKDIR /app

RUN python manage.py collectstatic --noinput

# entrypoint, must be executable file chmod +x entrypoint.sh
COPY ./scripts/entrypoint.sh ./scripts/start.sh ./scripts/gunicorn.sh /

CMD ["/start.sh"]
