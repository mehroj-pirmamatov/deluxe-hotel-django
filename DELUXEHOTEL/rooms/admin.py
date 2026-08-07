from django.contrib import admin
from unfold.admin import ModelAdmin
from.models import RoomType, Rooms

@admin.register(RoomType)
class RoomTypeAdmin(ModelAdmin):

    list_display=("room_type","created_at")
    list_filter=("created_at",)
    ordering=("-created_at",)


@admin.register(Rooms)
class RoomsAdmin(admin.ModelAdmin):

    list_display=("room_type","people","price","created_at")
    list_filter=("created_at",)
    search_fields=("view",)
    ordering=("-created_at",)