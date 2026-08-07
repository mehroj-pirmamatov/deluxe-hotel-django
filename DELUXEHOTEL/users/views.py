from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages


def Login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('overview')
        else:
            messages.info(request, "Username or Password is incorrect")
    context = {}
    return render(request, "auth/admin-login.html", context)


def Logout_view(request):
    logout(request)
    return redirect("index")
