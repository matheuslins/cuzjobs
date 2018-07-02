import django_heroku

from .common import *


ALLOWED_HOSTS = ['cuscuzjobs.herokuapp.com', 'cuscuzjobs.com.br']

DEBUG = False

django_heroku.settings(locals())
