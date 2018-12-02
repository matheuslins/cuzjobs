import requests
import operator

from furl import furl
from django.views.generic import ListView

from allauth.socialaccount.models import SocialAccount, SocialToken
from decouple import config

from users_auth.models import DefaultUser
from job.serializer import JobSerializer
from job.models import Job
from core.constants import REPOS_URL


class DashboardView(ListView):
    template_name = "dashboard.html"
    serializer_class = JobSerializer

    def get_queryset(self):
        pass

    def get(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        context = self.get_context_data()
        # user_exists = DefaultUser.objects.filter(username=request.user.username).exists()
        ranking_languages = {}
        # Fazer consulta no banco
        user_repos = False
        username = request.user.username

        if not user_repos:
            repos = requests.get(REPOS_URL(user=username, id=config('GITHUB_KEY'), secret=config('GITHUB_SECRET')))
            if repos.ok:
                for repo in repos.json():
                    keys = {'client_id': config('GITHUB_KEY'), 'client_secret': config('GITHUB_SECRET')}
                    url_langueges = furl(repo.get('languages_url')).add(keys).url
                    languages_stats = requests.get(url_langueges).json()
                    [ranking_languages.setdefault(language, []).append(stat) \
                        for language, stat in languages_stats.items()]

                top_languages = {language: len(numbers) for language, numbers in ranking_languages.items()}
                context.update({
                    'top_languages':  sorted(top_languages.items(), key=operator.itemgetter(1), reverse=True)
                })

        return self.render_to_response(context)

