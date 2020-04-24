from django.urls import path
from django.contrib.auth.decorators import login_required

from .views import CreateJobAPI, AllJobsHandler, RetrieveUpdateJobAPI, JobsNextToYouHandler


urlpatterns = [
    path(
        '<int:job_id>',
        login_required(RetrieveUpdateJobAPI.as_view()),
        name='retrieve_update'
    ),
    path(
        'create/',
        login_required(CreateJobAPI.as_view()),
        name='create'
    ),
    path(
        'all-jobs/',
        login_required(AllJobsHandler.as_view()),
        name='all_jobs'
    ),
    path(
        'next-to-you/',
        login_required(JobsNextToYouHandler.as_view()),
        name='next_to_you'
    )
]
