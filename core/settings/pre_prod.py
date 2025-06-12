from .base import *

DEBUG = os.environ.get('DEBUG', default=0)

ADMINS = [('PrzemysławL', 'przlutowski@gmail.com')]

ALLOWED_HOSTS = os.environ.get('DJANGO_ALLOWED_HOSTS', default=[]).split(' ')

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'my_website_dev_db',
#         'USER': 'my_website_dev_user',
#         'PASSWORD': 'Banzai123!',
#         'HOST': '195.238.122.125',
#         'PORT': '5432',
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': os.environ.get('POSTGRES_ENGINE', 'django.db.backends.postgresql_psycopg2'),
        'NAME': os.environ.get('POSTGRES_DB', 'name'),
        'USER': os.environ.get('POSTGRES_USER', 'user'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD', 'password'),
        'HOST': '195.238.122.125',
        'PORT': os.environ.get('POSTGRES_PORT', '5432'),
    }
}