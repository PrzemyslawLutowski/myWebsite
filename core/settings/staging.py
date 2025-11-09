from .base import *

CSRF_TRUSTED_ORIGINS = ['https://*.195.238.122.125:8072', 'https://195.238.122.125:8072']
CSRF_COOKIE_DOMAIN = 'https://195.238.122.125:8072'

# DEBUG = os.environ.get('DEBUG', default=0)
#
# ADMINS = [('PrzemysławL', 'przlutowski@gmail.com')]
#
# ALLOWED_HOSTS = os.environ.get('DJANGO_ALLOWED_HOSTS', default=[]).split(' ')
