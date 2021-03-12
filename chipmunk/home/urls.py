from django.urls import path

from .views import home, login_view, register

urlpatterns = [
    path("register", register, name="register"),
    path("login", login_view, name="login"),
    path("", home, name="home"),
]
