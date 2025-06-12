from .base import *

DEBUG = os.environ.get('DEBUG', default=0)

ADMINS = [('PrzemysławL', 'przlutowski@gmail.com')]

# ALLOWED_HOSTS = os.environ.get('DJANGO_ALLOWED_HOSTS', default=[]).split(' ')
ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': os.environ.get('POSTGRES_ENGINE', 'django.db.backends.postgresql_psycopg2'),
        'NAME': os.environ.get('POSTGRES_DATABASE', 'name'),
        'USER': os.environ.get('POSTGRES_USER', 'user'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD', 'password'),
        # 'HOST': os.environ.get('POSTGRES_HOST', 'localhost'),
        # 'PORT': os.environ.get('POSTGRES_PORT', '5432'),
    }
}