from django.contrib import admin

from .models import Choice, Question

# Register your models here to CRUD them from admin site
admin.site.register(Question)
admin.site.register(Choice)
