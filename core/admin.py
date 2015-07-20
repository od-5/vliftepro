from django.contrib import admin
from .models import Setup

__autor__ ='alexy'


class SetupAdmin(admin.ModelAdmin):
    list_display = ('title', 'email', 'phone')

admin.site.register(Setup, SetupAdmin)