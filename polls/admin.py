from django.contrib import admin
from .models import Question, Choice

# Register your models here to CRUD them from admin site
admin.site.register(Question)
admin.site.register(Choice)
