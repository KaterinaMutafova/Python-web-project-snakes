from django.contrib import admin
from .models import Python

# Register your models here.


class PythonAdmin(admin.ModelAdmin):
    fields = ['name', 'description', 'image']
    list_display = ['name', 'description', 'image']
    list_filter = ['name', 'description', 'image']



admin.site.register(Python, PythonAdmin)