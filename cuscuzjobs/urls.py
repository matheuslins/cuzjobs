from django.contrib import admin
from django.urls import path, include
from allauth.account.views import login


urlpatterns = [
    path('', include('allauth.urls')),
    path("", login, name="account_login"),
    path('auth/', include(('users_auth.urls', 'users_auth'), namespace='auth')),
    path('job/', include(('job.urls', 'users_auth'), namespace='job')),
    path('admin/', admin.site.urls)
]
