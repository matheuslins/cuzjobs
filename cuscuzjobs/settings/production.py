import django_heroku

from .common import *


ALLOWED_HOSTS = ['*']

DEBUG = True

django_heroku.settings(locals())
