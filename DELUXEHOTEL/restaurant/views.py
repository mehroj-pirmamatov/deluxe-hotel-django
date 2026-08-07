from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from.models import Menu

class RestaurantView(ListView):
    template_name = "restaurants/restaurant.html"

    def get_queryset(self):
        return Menu.objects.all()
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["menues"] =Menu.objects.all()
        return context
    