from django.urls import path

from .views import CreateJobAPI, AllJobsHandler, RetrieveUpdateJobAPI, JobsNextToYouHandler


urlpatterns = [
    path(
        '<int:job_id>',
        RetrieveUpdateJobAPI.as_view(),
        name='retrieve_update'
    ),
    path(
        'create/',
        CreateJobAPI.as_view(),
        name='create'
    ),
    path(
        'all-jobs/',
        AllJobsHandler.as_view(),
        name='all_jobs'
    ),
    path(
        'next-to-you/',
        JobsNextToYouHandler.as_view(),
        name='next_to_you'
    )
]
