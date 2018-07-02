import os
import importlib

from django.conf import settings
from apistar import Include, Route


def find_routes():
    routes = []
    apps_include = []
    for root, dirs, files in os.walk("."):
        url = '/api'
        if 'routes.py' in files:
            path = root.replace('/', '.').split('..')[1] + '.routes'
            for app in settings.PROJECT_APPS:
                if app in path:
                    app_name = app
            try:
                file_routes = getattr(
                    importlib.import_module(path), 'routes')
            except Exception as e:
                print(e)
            for file_route in file_routes:
                root_file = file_route.get('url')
                try:
                    if root_file != '/api':
                        url = '/api/' + app_name
                    routes.append(Route(**file_route))
                except Exception as e:
                    raise Exception(f"Route {e} in <path>: {path}")
            include_params = {'url': url,
                              'name': url, 'routes': routes}
            apps_include.append(Include(**include_params))
            routes = []
    return apps_include
