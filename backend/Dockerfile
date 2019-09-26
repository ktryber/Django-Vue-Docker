FROM python:3

# python dependencies
COPY ./requirements.txt /
RUN pip install -r ./requirements.txt
COPY . .
# upload scripts
COPY ./scripts/entrypoint.sh ./scripts/start.sh ./scripts/gunicorn.sh /


CMD ["/gunicorn.sh"]