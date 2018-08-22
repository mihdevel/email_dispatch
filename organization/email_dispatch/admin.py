from django.contrib import admin
from .models import Email, Dispatch, Group, Template, Report

admin.site.register(Email)
admin.site.register(Group)
admin.site.register(Dispatch)
admin.site.register(Template)
admin.site.register(Report)
