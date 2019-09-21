FROM python:3

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt /app

RUN pip install -r requirements.txt

COPY . /app

# entrypoint, must be executable file chmod +x dev.entrypoint.sh
COPY ./scripts/dev.entrypoint.sh /

CMD ["/dev.entrypoint.sh"]
