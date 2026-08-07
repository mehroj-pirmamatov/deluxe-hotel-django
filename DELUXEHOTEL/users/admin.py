from django.contrib import admin
from django.contrib.auth.models import User
from unfold.admin import ModelAdmin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

try:
    admin.site.unregister(User)
except admin.sites.NotRegistered:
    pass

@admin.register(User)
class CustomUser(BaseUserAdmin,ModelAdmin):
    pass
