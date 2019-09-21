#!/bin/bash

./manage.py collectstatic --noinput --settings=config.settings.production
./manage.py migrate --settings=config.settings.production
./manage.py runserver 0.0.0.0:8000 --settings=config.settings.production
