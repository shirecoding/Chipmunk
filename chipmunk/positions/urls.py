from django.urls import path

from .views import home, position

urlpatterns = [path("", home, name="home"), path("position", position, name="position")]
