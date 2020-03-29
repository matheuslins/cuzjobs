from django.urls import path

from .views import DashboardView, ProfileReport, Profile


urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),
    path('profile', Profile.as_view(), name='profile'),
    path('profile-report', ProfileReport.as_view(), name='profile_report')
]
