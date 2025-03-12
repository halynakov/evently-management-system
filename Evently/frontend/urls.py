from django.urls import path
from . import views

urlpatterns = [
  path("", views.index),
  path("events/", views.events, name="events"),
  path("home/", views.home, name="home"),
  path("sign-up/", views.signup, name="sign-up"),
  path("log-in/", views.login, name="log-in"),
  path("adminTest/", views.admin, name="adminTest"),
  path("adminTest/addPost", views.adminAddPost, name="adminAddPost"),
  path("adminTest/changePost", views.adminChengePost, name="adminChengePost"),
]
