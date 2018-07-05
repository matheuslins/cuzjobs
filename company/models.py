from django.db import models


class Company(models.Model):

    name = models.CharField(max_length=100, verbose_name='Name')
    company_type = models.CharField(max_length=100, verbose_name='Type',
                                    null=True, blank=True)
    company_size = models.CharField(max_length=100, verbose_name='Size',
                                    null=True, blank=True)
    industry = models.CharField(max_length=100, verbose_name='Industry',
                                null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name or "[Not set]")

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'
