from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.Snippet)
class SnippetsAdmin(admin.ModelAdmin):
    pass
