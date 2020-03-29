import time
import requests
import operator

from furl import furl
from django.views.generic import ListView, TemplateView

from decouple import config

from job.models import Job
from repository.models import Repository, Owner
from core.constants import REPOS_URL, COUNT_FILES_URL


class DashboardView(ListView):
    template_name = "dashboard.html"
    context = {}
    auth_keys = {'client_id': config('GITHUB_KEY'), 'client_secret': config('GITHUB_SECRET')}
    user_level = ''
    languages_infos = {}
    object_list = []

    def set_lang_level_by_skill(self, user):
        score_lang = {}
        metrics = {}
        stars = {}
        forks = {}
        watchers = {}
        issues = {}
        contributors = {}
        score_language = {}
        repos_user, top_langs = self.get_repos_user(user), self.context['top_languages']
        top_langs = [lang[0] for lang in top_langs]

        for repo in repos_user:
            # if repository isn't forked and has one of top languages
            if not repo.fork:
                for lang in top_langs:
                    if lang in repo.languages:
                        stars.setdefault(lang, []).append(repo.stargazers_count)
                        forks.setdefault(lang, []).append(repo.forks)
                        watchers.setdefault(lang, []).append(repo.watchers)
                        issues.setdefault(lang, []).append(repo.issues)
                        contributors.setdefault(lang, []).append(repo.contributors)
                        score_language.setdefault(lang, []).append(repo.score_languages[lang])

        for lang in top_langs:
            data = {
                'stars': sum(stars[lang]),
                'forks': sum(forks[lang]),
                'watchers': sum(watchers[lang]),
                'issues': sum(issues[lang]),
                'contributors': sum(contributors[lang]),
                'score_language': sum(score_language[lang]),
                'count_repos': len(stars[lang])
            }
            metrics.setdefault(lang, {}).update(data)

        for lang, metric in metrics.items():
            pondera = [
                metric['stars']*14,
                metric['forks']*16,
                metric['count_repos']*10,
                metric['watchers']*13,
                metric['issues']*18,
                metric['contributors']*22,
                metric['score_language']*7
            ]
            score = int(sum(pondera) / len(pondera))
            score_lang.update({lang: score})

        self.context.update({'score_lang': list(sorted(score_lang.items(), key=operator.itemgetter(1), reverse=True))[:4]})
        self.context.update({'level_lang': self.set_level(score_lang)})

    def set_level(self, score_lang):
        level_lang = {}
        level = ''
        for lang, score in score_lang.items():
            if score <=200:
                level = 'Iniciante'
            elif score > 200 and score <= 400:
                level = 'Júnior'
            elif score > 400 and score <= 600:
                level = 'Pleno'
            elif score > 600 and score <= 800:
                level = 'Sênior'
            elif (score > 800 and score <= 1000) or (score > 1000):
                level = 'Especialista'
            level_lang.update({lang: level})
        return level_lang

    def _queryset(self):
        jobs_by_languages = {}
        languages = self.context['top_languages']
        for language in languages:
            jobs_found = Job.objects.filter(technologies__contains=[language[0].lower()])
            [jobs_by_languages.setdefault(language[0], []).append(job) for job in jobs_found]
        filter_query_set = {'jobs_by_languages': jobs_by_languages}
        self.context.update(filter_query_set)
        return self.context

    def get_top_language(self):
        top_languages = {}
        languages_infos = self.languages_infos.copy()
        for language, numbers in languages_infos.items():
            score_lang = sum(numbers)
            result = {language: (score_lang, len(numbers))}
            top_languages.update(result)
        return {
            'top_languages': list(sorted(top_languages.items(), key=operator.itemgetter(1), reverse=True))[:4]
        }

    def iter_by_lang_repo(self, languages_stats, user, repo):
        score_languages = {}
        for lang in languages_stats.keys():
            kwargs_url = self.auth_keys.copy()
            kwargs_url.update({
                'user': user,
                'reponame': repo['name'],
                'lang': lang.lower()
            })
            url_count = COUNT_FILES_URL(**kwargs_url)
            search_code = requests.get(url_count).json()
            if not search_code or search_code.get('incomplete_results'):
                time.sleep(2)
                self.iter_by_lang_repo(languages_stats, user, repo)

            scores = [item.get('score', 0) for item in search_code.get('items', [])]
            if not len(scores) == 0:
                middle_score = int(sum(scores))
            else:
                middle_score = 0
            score_languages.update({lang: middle_score})
            # if repository isn't forked
            if not repo['fork']:
                self.languages_infos.setdefault(lang, []).append(middle_score)

        return score_languages

    @staticmethod
    def get_repos_user(user):
        return Repository.objects.filter(owner__login=user)

    def get(self, request, *args, **kwargs):
        user = request.user.username
        if user:
            repos_user = self.get_repos_user(user)

            if not repos_user.exists():
                repos = requests.get(REPOS_URL(user=user, id=config('GITHUB_KEY'), secret=config('GITHUB_SECRET')))
                for repo in repos.json():
                    url_languages = furl(repo.get('languages_url')).add(self.auth_keys).url
                    languages_stats = requests.get(url_languages).json()
                    score_languages = self.iter_by_lang_repo(languages_stats, user, repo)
                    self.create_repo(repo, languages_stats, score_languages)

            else:
                self.languages_infos = {}
                for repo in repos_user:
                    if not repo.fork:
                        languages_stats = repo.score_languages
                        [
                            self.languages_infos.setdefault(language, []).append(stat)
                            for language, stat in languages_stats.items()
                        ]

            self.context.update(self.get_top_language())
            self.set_lang_level_by_skill(user)
            self.object_list = self._queryset()
            context = self.get_context_data()
            context.update(self.context)

            return self.render_to_response(context)

        context = self.get_context_data(object_list=[])

        return self.render_to_response(context)

    def create_repo(self, repo, languages_stats, score_languages):
        payload_owner = {
            'login': repo['owner']['login'],
            'html_url': repo['owner']['html_url'],
            'avatar': repo['owner']['avatar_url']
        }

        filter_owner = Owner.objects.filter(login=repo['owner']['login'])
        if not filter_owner:
            owner_obj = Owner.objects.create(**payload_owner)
        else:
            owner_obj = filter_owner.first()

        url_contributors = furl(repo.get('contributors_url')).add(self.auth_keys).url
        contributors = requests.get(url_contributors).json()

        payload_repo = {
            'name': repo['name'],
            'html_url': repo['html_url'],
            'owner': owner_obj,
            'description': repo['description'],
            'languages': languages_stats,
            'score_languages': score_languages,
            'fork': repo['fork'],
            'forks': repo['forks_count'],
            'issues': repo['open_issues_count'],
            'contributors': (len(contributors) - 1) if contributors else 0,
            'watchers': repo['watchers'],
            'stargazers_count': repo['stargazers_count'],
            'has_wiki': repo['has_wiki'],
            'created_at': repo['created_at'],
            'updated_at': repo['updated_at']
        }

        repository = Repository.objects.filter(**payload_repo)
        if not repository:
            Repository.objects.create(**payload_repo)


class ProfileReport(ListView):
    template_name = "profile_report.html"
    context = {}

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.object_list = self._queryset()

    @staticmethod
    def _queryset():
        return Job.objects.all()

    def get(self, request, *args, **kwargs):
        self.context.update({
            'jobs': self.object_list
        })
        return self.render_to_response(self.context)


class Profile(TemplateView):
    template_name = "profile.html"
    context = {}
