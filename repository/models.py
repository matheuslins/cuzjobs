from django.db import models


class Owner(models.Model):
    name = models.CharField('Nome', max_length=100)
    login = models.CharField('Login', max_length=100)
    avatar = models.ImageField(upload_to='repository/images', verbose_name='Imagem', null=True, blank=True)
    url_gh = models.CharField('Url GitHub', max_length=300, null=True, blank=True)

    def __str__(self):
        return str(self.name or "[Not set]")

    class Meta:
        verbose_name = 'Owner'
        verbose_name_plural = 'Owners'


class Repository(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nome')
    stars = models.IntegerField('Estrelas')
    owner = models.ForeignKey(
        Owner,
        on_delete=models.CASCADE,
        related_name="repository_owner",
        verbose_name="Owner"
    )
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name or "[Not set]")

    class Meta:
        verbose_name = 'Repository'
        verbose_name_plural = 'Repositories'
