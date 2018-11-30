from django.contrib import admin

from .models import *

admin.site.register(DefaultUser)
admin.site.register(TechRecruiter)
admin.site.register(Candidate)
