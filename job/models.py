from django.db import models
from django.contrib.postgres.fields import ArrayField

from company.models import Company
from users_auth.models import Candidate


class Job(models.Model):
    job_id = models.IntegerField()
    _type = models.CharField(max_length=100, verbose_name='Type',
                             null=True, blank=True)
    title = models.CharField(max_length=100, verbose_name='Title')
    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name="job_company",
        verbose_name="Company"
    )
    benefits = ArrayField(
        models.CharField(max_length=200, verbose_name='Benefits'),
        blank=True, null=True
    )
    tecnologies = ArrayField(models.CharField(max_length=200, verbose_name='Tecnologies'), blank=True, null=True)
    location = models.CharField(max_length=100, verbose_name='Location', null=True, blank=True)
    experience_level = models.CharField(max_length=100, verbose_name='Experience Lvel', null=True, blank=True)
    role = models.CharField(max_length=100, verbose_name='Role', null=True, blank=True)
    industry = models.CharField(max_length=100, verbose_name='Industry', null=True, blank=True)
    salary = models.CharField(max_length=100, verbose_name='salary', null=True, blank=True)
    sponsor = models.CharField(max_length=100, verbose_name='Sponsor', null=True, blank=True)
    paid = models.CharField(max_length=100, verbose_name='Paid', null=True, blank=True)
    description = models.TextField(null=True, blank=True, verbose_name='Description')
    link_apply = models.CharField(max_length=800, verbose_name='Link to Apply', null=True, blank=True)
    url = models.CharField(max_length=800, verbose_name='Url', null=True, blank=True)

    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.title or "[Not set]")

    class Meta:
        verbose_name = 'Job'
        verbose_name_plural = 'Jobs'


class JobCandidate(models.Model):
    job = models.ForeignKey(
        Job,
        on_delete=models.CASCADE,
        related_name="jc_job",
        verbose_name="Job"
    )
    candidate = models.ForeignKey(
        Candidate,
        on_delete=models.CASCADE,
        related_name="jc_candidate",
        verbose_name="Candidate"
    )

    def __str__(self):
        return str(
            self.job.job_id or "[Not set]") + '->' + str(
                self.candidate.name or "[Not set]")

    class Meta:
        verbose_name = 'Job of Candidate'
        verbose_name_plural = 'Jobs of Candidates'
