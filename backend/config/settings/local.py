from .base import *
from .base import env

ALLOWED_HOSTS = ["*"]

SECRET_KEY = env('SECRET_KEY', default='super-secret')

DEBUG = env.bool('DEBUG', False)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env('PG_NAME'),
        'USER': env('PG_USER'),
        'HOST': env('PG_HOST'),
        'PORT': env('PG_PORT'),
    }
}
