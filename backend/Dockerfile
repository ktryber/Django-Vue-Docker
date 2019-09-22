FROM python:3

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt /

RUN pip install -r /requirements.txt

COPY . /app
# collect static files
RUN python manage.py collectstatic --noinput

# entrypoint, must be executable file chmod +x entrypoint.sh
COPY ./scripts/entrypoint.sh /

CMD ["/entrypoint.sh"]