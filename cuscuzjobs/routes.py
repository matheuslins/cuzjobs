from cuscuzjobs.views import home


routes = [
    {
        'url': '/api',
        'method': 'GET',
        'handler': home
    }
]
