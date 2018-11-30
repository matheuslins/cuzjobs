from django.contrib import admin

from .models import Job
from .models import JobCandidate


class JobAdmin(admin.ModelAdmin):
    ordering = ['date_created']
    search_fields = ['title']

admin.site.register(Job, JobAdmin)
admin.site.register(JobCandidate)
