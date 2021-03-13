from django.contrib import messages
from django.contrib.auth import authenticate
from django.shortcuts import redirect, render

from .forms import SignUpForm


def signup(request):

    if request.user.is_authenticated:
        return redirect("/")

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"{username} is now registered !")
            return redirect("/accounts/login")
        else:
            messages.error(request, form.errors)
            return render(request, "registration/signup.html", {"form": form})

    else:
        form = SignUpForm()
        return render(request, "registration/signup.html", {"form": form})
