from django.urls import path

from .views import CreateJobAPI, ListJobAPI, RetrieveUpdateJobAPI


urlpatterns = [
    path('<int:job_id>',
         RetrieveUpdateJobAPI.as_view(),
         name='retrieve_update'
    ),
    path('create/',
         CreateJobAPI.as_view(),
         name='create'
    ),
    path('list/',
        ListJobAPI.as_view(),
        name='list'
    )
]
