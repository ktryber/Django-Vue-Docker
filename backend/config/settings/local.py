from .base import *
import os

ALLOWED_HOSTS = ["*"]

SECRET_KEY = os.environ.get('SECRET_KEY', default='super-secret')

DEBUG = os.environ.get('DEBUG', False)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('PG_NAME', 'postgres'),
        'USER': os.environ.get('PG_USER', 'postgres'),
        'PASSWORD': os.environ.get('PG_PASSWORD', 'postgres_password'),
        'HOST': os.environ.get('PG_HOST', 'db'),
        'PORT': os.environ.get('PG_PORT', '5432'),
    }
}
