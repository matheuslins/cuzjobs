from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include(('core.urls', 'core'), namespace='core')),
    path('users_auth/', include(('users_auth.urls', 'users_auth'), namespace='users_auth')),
    path('job/', include(('job.urls', 'job'), namespace='job')),

    path('accounts/', include('allauth.urls')),
    path('admin/', admin.site.urls)

]
