from django.contrib import admin
from django.urls import path, include
from allauth.account import views


urlpatterns = [
    path('', include('allauth.urls')),
    path("", views.login, name="account_login"),
    path('auth/', include(('users_auth.urls', 'users_auth'), namespace='auth')),
    path('job/', include(('job.urls', 'users_auth'), namespace='job')),
    path('admin/', admin.site.urls)
]
