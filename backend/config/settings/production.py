import os
from .base import *

ALLOWED_HOSTS = ["*"]
SECRET_KEY = os.environ.get('SECRET_KEY', default='super-secret')

DEBUG = os.environ.get('DEBUG', False)


if 'RDS_HOSTNAME' in os.environ:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.environ['RDS_DB_NAME'],
            'USER': os.environ['RDS_USERNAME'],
            'PASSWORD': os.environ['RDS_PASSWORD'],
            'HOST': os.environ['RDS_HOSTNAME'],
            'PORT': os.environ['RDS_PORT'],
        }
    }
