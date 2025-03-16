from django.urls import path
from .views import RegisterView, registration_page, verify_user, login_view, logout_view

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("register_page/", registration_page, name="register_page"),
    path("verify/<uuid:token>/", verify_user, name="verify"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
]
