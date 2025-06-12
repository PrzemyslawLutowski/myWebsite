from .base import *

DEBUG = os.environ.get('DEBUG', default=0)

ADMINS = [('PrzemysławL', 'przlutowski@gmail.com')]

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('POSTGRES_DB', 'name'),
        'USER': os.environ.get('POSTGRES_USER', 'user'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD', 'password'),
        # 'HOST': '195.238.122.125',
        # 'PORT': '5432',
    }
}