from django.urls import path
from django.contrib.auth import views as auth_views

from .views import HomeView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('login', auth_views.login, {'template_name': 'login.html'}, name='login'),
    path('logout', auth_views.logout, {'next_page': 'core:login'}, name='logout')
]
