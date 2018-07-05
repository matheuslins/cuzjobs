from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include(('core.urls', 'core'), namespace='core')),
    path('account/', include(
        ('account.urls', 'account'), namespace='account')),
    path('job/', include(
        ('job.urls', 'account'), namespace='job')),
    path('admin/', admin.site.urls)
]
