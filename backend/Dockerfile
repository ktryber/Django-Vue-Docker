FROM python:3

# python envs
ENV PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=10

COPY ./requirements.txt /

RUN pip install -r ./requirements.txt

COPY . /app
# collect static files
WORKDIR /app

RUN python manage.py collectstatic --noinput

# entrypoint, must be executable file chmod +x entrypoint.sh
COPY ./scripts/entrypoint.sh ./scripts/start.sh ./scripts/gunicorn.sh /



CMD ["/gunicorn.sh"]

ENTRYPOINT [ "/start.sh" ]