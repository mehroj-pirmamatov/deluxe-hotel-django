from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from.models import Rooms

class RoomView(TemplateView):
    template_name = "rooms/rooms.html"

    def get_queryset(self):
        return Rooms.objects.all()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["rooms"] = Rooms.objects.all()
        return context
    
    
