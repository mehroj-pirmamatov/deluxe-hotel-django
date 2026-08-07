from django.urls import path
from.views import BlogView, BlogSingleView

urlpatterns = [
    path("",BlogView.as_view(),name="blog"),
    path("blog/single/<int:pk>",BlogSingleView.as_view(),name="blog-single"),

]