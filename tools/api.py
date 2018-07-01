import os
import importlib

from apistar import Route


def find_routes():
    routes = []
    for root, dirs, files in os.walk("."):
        if 'routes.py' in files:
            path = root.replace('/', '.').split('..')[1] + '.routes'
            try:
                file_routes = getattr(importlib.import_module(path), 'routes')
            except Exception as e:
                print(e)

            for file_route in file_routes:
                try:
                    routes.append(Route(**file_route))
                except Exception as e:
                    raise Exception(f"Route {e} in <path>: {path}")

    if not routes:
        raise Exception("Your app needs a file called routes.py")

    return routes
