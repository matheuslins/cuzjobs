import django_heroku

from .common import *


ALLOWED_HOSTS = ['*']

DEBUG = False

django_heroku.settings(locals())
