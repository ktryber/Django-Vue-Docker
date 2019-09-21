from .base import *
import os

ALLOWED_HOSTS = ["*"]

SECRET_KEY = config('SECRET_KEY', default='super-secret')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('PG_NAME', default='postgres'),
        'USER': config('PG_USER', default='postgres'),
        'PASSWORD': config('PG_PASSWORD', default='postgrespassword'),
        'HOST': config('PG_HOST', default='db'),
        'PORT': config('PG_PORT', default=5432),
    }
}
