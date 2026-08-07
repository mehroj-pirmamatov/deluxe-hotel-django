from django.contrib import admin
from .models import Blog

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display=("id","title")
    list_filter=("created_at",)
    ordering=("created_at",)
