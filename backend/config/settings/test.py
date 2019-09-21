from .base import *

import os

ALLOWED_HOSTS = ["*"]

SECRET_KEY = os.environ.get('SECRET_KEY', default='super-secret')

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'HOST': 'db',
        'PORT': 5432,
    }
}
