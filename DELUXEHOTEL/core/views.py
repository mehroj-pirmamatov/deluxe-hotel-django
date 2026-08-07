from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from blog.models import Blog
from rooms.models import Rooms

class IndexView(TemplateView):
    template_name="core/index.html"
    def get_queryset(self):
        return Blog.objects.all()
    

    def get_context_data(self, **kwargs):
        context=super().get_context_data( **kwargs)
        context["blogs"]=Blog.objects.all()
        context["rooms"]=Rooms.objects.all()
        return context

class AboutView(TemplateView):
    template_name="core/about.html"
