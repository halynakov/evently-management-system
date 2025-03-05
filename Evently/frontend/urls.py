from django.urls import path
from . import views

urlpatterns = [
  path("", views.index),
  path("events/", views.events, name="events"),
  path("home/", views.home, name="home"),
  path("logup/", views.logup, name="logup"),
  path("login/", views.login, name="login"),
  path("adminTest/addPost", views.adminAddPost, name="adminAddPost"),
  path("adminTest/changePost", views.adminChengePost, name="adminChengePost"),
]
