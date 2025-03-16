from django.urls import path

from verification.views import RegisterView, registration_page, verify_user, login_view
from . import views

urlpatterns = [
  path("", views.index),
  path("events/", views.events, name="events"),
  path("home/", views.home, name="home"),
  #path("sign-up/", views.signup, name="sign-up"),
  path("register/", RegisterView.as_view(), name="register"),
  path("sign-up/", registration_page, name="sign-up"),
  path("log-in/", views.login, name="log-in"),
  path("adminTest/addPost", views.adminAddPost, name="adminAddPost"),
  path("adminTest/changePost", views.adminChengePost, name="adminChengePost"),
]
