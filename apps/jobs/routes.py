from .receivers import create_job, get_jobs


routes = [
    {
        'url': '/create-job/',
        'method': 'POST',
        'handler': create_job
    },
    {
        'url': '/jobs',
        'method': 'GET',
        'handler': get_jobs
    }
]
