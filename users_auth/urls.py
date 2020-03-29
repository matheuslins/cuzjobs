from django.urls import path

from .views import DashboardView, ProfileReport


urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),
    path('profile-report', ProfileReport.as_view(), name='profile_report')
]
