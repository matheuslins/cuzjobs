import dj_database_url
import django_heroku

from dj_database_url import parse as db_url
from decouple import config

from .common import *

# ALLOWED_HOSTS = ['cuscuzjobs.herokuapp.com', 'cuscuzjobs.com.br']

# DATABASES = {
#     'default': config('DATABASE_URL', cast=db_url)
# }

# db_from_env = dj_database_url.config()
# DATABASES['default'].update(db_from_env)

# DEBUG = False

django_heroku.settings(locals())
