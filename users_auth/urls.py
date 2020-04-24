from django.urls import path

from django.contrib.auth.decorators import login_required

from .views import DashboardView, ProfileReport, Profile


urlpatterns = [
    path('', login_required(DashboardView.as_view()), name='dashboard'),
    path('profile', login_required(Profile.as_view()), name='profile'),
    path('profile-report', login_required(ProfileReport.as_view()), name='profile_report')
]
