FROM python:3

# python dependencies
COPY ./requirements.txt /
RUN pip install -r ./requirements.txt
COPY . /app


# upload scripts
COPY ./scripts/entrypoint.sh ./scripts/start.sh ./scripts/gunicorn.sh /
WORKDIR /app
RUN python manage.py collectstatic --noinput

EXPOSE 8000

ENTRYPOINT ["/gunicorn.sh"]