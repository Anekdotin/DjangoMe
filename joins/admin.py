from django.contrib import admin

# Register your models here.
from .models import Join


class JoinAdmin(admin.ModelAdmin):
    list_display = ['__unicode__', 'email', 'created', 'updated']

    class Meta:
        modelList = Join

admin.site.register(Join)