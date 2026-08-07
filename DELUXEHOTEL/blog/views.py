from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import Blog

class BlogView(ListView):
    template_name = "blog/blog.html"
    context_object_name="blogs"
    paginate_by=8

    def get_queryset(self):
        return Blog.objects.all().order_by("-created_at")
    
    def get_context_data(self, **kwargs):
        context=super().get_context_data( **kwargs)
        context["blog_count"]=Blog.objects.all().count()
        return context
    
    
    

class BlogSingleView(DetailView):

    template_name = "blog/blog-single.html"
    context_object_name="blog_single"

    def get_queryset(self):
        return Blog.objects.all()
    
    def get_context_data(self, **kwargs):
        context=super().get_context_data( **kwargs)
        context["blog_count"]=Blog.objects.all().count()
        context["blogs"]=Blog.objects.all()
        return context
