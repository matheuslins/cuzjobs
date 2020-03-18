from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include(('core.urls', 'core'), namespace='core')),
    path('auth/', include(('users_auth.urls', 'users_auth'), namespace='auth')),
    path('job/', include(('job.urls', 'users_auth'), namespace='job')),

    path('accounts/', include('allauth.urls')),
    path('admin/', admin.site.urls)

]
