from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render

from .forms import RegistrationForm


def home(request):
    return render(request, "home/home.html", {})


def register(request):

    if request.user.is_authenticated:
        return redirect("/")

    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"{username} is now registered !")
            return redirect("login")
        else:
            messages.error(request, form.errors)
            return render(request, "forms/register.html", {"form": form})

    else:
        form = RegistrationForm()
        return render(request, "forms/register.html", {"form": form})


def login_view(request):

    if request.user.is_authenticated:
        return redirect("/")

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect("/")
        else:
            messages.error(request, "username or password is incorrect")
            return render(request, "forms/login.html", {})

    else:
        return render(request, "forms/login.html", {})
