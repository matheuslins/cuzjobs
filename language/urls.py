from django.urls import path

from .views import LanguagesListView, LanguagesDetailView


urlpatterns = [
    path('list', LanguagesListView.as_view(), name='list'),
    path('detail', LanguagesDetailView.as_view(), name='detail')
]
