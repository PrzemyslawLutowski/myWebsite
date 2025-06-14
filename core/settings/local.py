from .base import *


DEBUG = os.environ.get('DEBUG', default=0)

ALLOWED_HOSTS = os.environ.get('DJANGO_ALLOWED_HOSTS', default=[]).split(' ')

