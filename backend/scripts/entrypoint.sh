#!/bin/bash

./manage.py collectstatic --noinput --settings=config.settings.production
# i commit my migration files to git so i dont need to run it on server
# ./manage.py makemigrations app_name
./manage.py migrate --settings=config.settings.production
./manage.py runserver 0.0.0.0:8000 --settings=config.settings.production
