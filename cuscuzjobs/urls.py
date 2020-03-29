from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('allauth.urls')),
    path('auth/', include(('users_auth.urls', 'users_auth'), namespace='auth')),
    path('job/', include(('job.urls', 'users_auth'), namespace='job')),
    path('admin/', admin.site.urls)
]
