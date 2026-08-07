from django.contrib import admin
from unfold.admin import ModelAdmin
from.models import Menu

@admin.register(Menu)
class MenuAdmin(ModelAdmin):

    list_display=("title","created_at")
    list_filter=("created_at",)
    ordering=("-created_at",)
