import os
import importlib

from apistar import ASyncApp, App
from decouple import config

from tools.api import find_routes


#############################
####### BASE SETTINGS #######
#############################

BASE_DIR = os.path.dirname(__file__)
HOST = config('HOST', cast=str, default='localhost')
PORT = config('PORT', cast=int, default=5000)
DEBUG = config('DEBUG', cast=bool, default=True)


params_settings = {
    'host': HOST,
    'port': PORT,
    'debug': DEBUG
}

#############################
####### APP SETTINGS ########
#############################

# TEMPLATES
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')

# STATIC_FILES
STATIC_DIR = os.path.join(BASE_DIR, 'static')

APPLICATION = config('TYPE_APP', cast=str, default='app')

args = {
    'routes': find_routes(),
    'template_dir': TEMPLATE_DIR,
    'static_dir': STATIC_DIR
}

if APPLICATION == 'async':
    application = ASyncApp
else:
    application = App

app = application(**args)
