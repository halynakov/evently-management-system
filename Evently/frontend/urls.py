from django.urls import path
from . import views

urlpatterns = [
  path("", views.index),
  path("events/", views.events, name="events"),
  path("home/", views.home, name="home"),
  path("sign-up/register", views.logup, name="sign-up"),
  path("log-in/", views.login, name="log-in"),
  path("adminTest/addPost", views.adminAddPost, name="adminAddPost"),
  path("adminTest/changePost", views.adminChengePost, name="adminChengePost"),
]
