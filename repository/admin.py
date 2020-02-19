from django.contrib import admin

from .models import Owner, Repository

admin.site.register(Owner)
admin.site.register(Repository)
