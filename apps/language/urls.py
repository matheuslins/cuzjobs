from django.urls import path

from django.contrib.auth.decorators import login_required

from .views import LanguagesListView, LanguagesDetailView


urlpatterns = [
    path('', login_required(LanguagesListView.as_view()), name='list'),
    path('<slug:language>', login_required(LanguagesDetailView.as_view()), name='detail')
]
