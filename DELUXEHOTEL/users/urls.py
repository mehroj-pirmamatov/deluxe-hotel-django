from django.urls import path

from .views import Login_view,Logout_view

urlpatterns = [
    path("login/",Login_view, name="login"),
    path("logout/",Logout_view, name="logout"),

]