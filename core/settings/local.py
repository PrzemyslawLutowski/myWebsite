from .base import *


DEBUG = os.environ.get('DEBUG', default=0)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'my_website_dev_db',
        'USER': 'my_website_dev_user',
        'PASSWORD': 'Banzai123!',
        'HOST': '195.238.122.125',
        'PORT': '5432',
    }
}