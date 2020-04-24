from django.contrib import admin
from django.urls import path, include
from allauth.account.views import login
from django.conf.urls.static import static
from cuscuzjobs.settings.common import MEDIA_ROOT, MEDIA_URL


urlpatterns = [
    path('', include('allauth.urls')),
    path('', login, name="account_login"),
    path('auth/', include(('users_auth.urls', 'users_auth'), namespace='auth')),
    path('job/', include(('job.urls', 'users_auth'), namespace='job')),
    path('languages/', include(('language.urls', 'language'), namespace="language")),
    path('admin/', admin.site.urls)
]

urlpatterns.extend(
    static(MEDIA_URL, document_root=MEDIA_ROOT)
)