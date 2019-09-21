from .base import *
# from .base import env

import os

ALLOWED_HOSTS = ["*"]

SECRET_KEY = os.environ.get('SECRET_KEY', default='super-secret')

DEBUG = os.environ.get('DEBUG', False)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('PG_NAME'),
        'USER': os.environ.get('PG_USER'),
        'HOST': os.environ.get('PG_HOST'),
        'PORT': os.environ.get('PG_PORT'),
    }
}
