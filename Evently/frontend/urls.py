from django.urls import path
from . import views

urlpatterns = [
  path("", views.index),
  path("events/", views.events, name="events"),
  path("home/", views.home, name="home")
]
