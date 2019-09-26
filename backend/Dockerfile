FROM python:3

# python dependencies
COPY ./requirements.txt /
RUN pip install -r ./requirements.txt
COPY . /app

RUN python manage.py collectstatic --noinput
# upload scripts
COPY ./scripts/entrypoint.sh ./scripts/start.sh ./scripts/gunicorn.sh /
WORKDIR /app

EXPOSE 8000

CMD ["/gunicorn.sh"]