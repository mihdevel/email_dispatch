from django.contrib import admin
from .models import Email, Dispatch, Group, Report

admin.site.register(Email)
admin.site.register(Group)
admin.site.register(Dispatch)
admin.site.register(Report)
