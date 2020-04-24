from django.urls import path

from .views import LanguagesListView, LanguagesDetailView


urlpatterns = [
    path('', LanguagesListView.as_view(), name='list'),
    path('<slug:language>', LanguagesDetailView.as_view(), name='detail')
]
