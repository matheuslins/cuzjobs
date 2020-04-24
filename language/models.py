from django.db import models


class Language(models.Model):
    name = models.CharField(max_length=200, verbose_name='Nome')
    key = models.CharField(max_length=100, verbose_name='Chave')
    image = models.ImageField(upload_to='assets/img/language', verbose_name='Imagem', null=True, blank=True)
    repositories = models.IntegerField(null=True, blank=True)
    stars = models.IntegerField(null=True, blank=True)
    watchers = models.IntegerField(null=True, blank=True)
    forks = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return str(self.name or "[Not set]")

    class Meta:
        verbose_name = 'Language'
        verbose_name_plural = 'Languages'
