from .receivers import home


routes = [
    {
        'url': '/',
        'method': 'GET',
        'handler': home
    }
]