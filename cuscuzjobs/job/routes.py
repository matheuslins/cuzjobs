from .views import create_job, get_jobs


routes = [
    {
        'url': '/api/create/',
        'method': 'POST',
        'handler': create_job
    },
    {
        'url': '/api/list',
        'method': 'GET',
        'handler': get_jobs
    }
]
