from django.db import models
from jsonfield import JSONField


class Owner(models.Model):
    login = models.CharField('Login', max_length=100)
    avatar = models.ImageField(upload_to='repository/images', verbose_name='Imagem', null=True, blank=True)
    html_url = models.CharField('Url GitHub', max_length=300, null=True, blank=True)

    def __str__(self):
        return str(self.login or "[Not set]")

    class Meta:
        verbose_name = 'Owner'
        verbose_name_plural = 'Owners'


class Repository(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nome')
    html_url = models.CharField('Url', max_length=300)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name="repository_owner", verbose_name="Owner")
    description = models.TextField('Descrição', blank=True, null=True)
    fork = models.BooleanField('É Forkado?', default=False)
    forks = models.IntegerField('Forks', default=0)
    watchers = models.IntegerField('Watchers', default=0)
    issues = models.IntegerField('Issues Reported', default=0)
    contributors = models.IntegerField('Quantidade de Contribuidores', default=0)
    stargazers_count = models.IntegerField('Estrelas', default=0)
    has_wiki = models.BooleanField('Tem Wiki?', default=False)
    languages = JSONField()
    score_languages = JSONField(default={})
    created_at = models.CharField('Criado em', max_length=100, blank=True, null=True)
    updated_at = models.CharField('Útima atualização', max_length=100, blank=True, null=True)

    def __str__(self):
        return str(self.name or "[Not set]")

    class Meta:
        verbose_name = 'Repository'
        verbose_name_plural = 'Repositories'
