from django.urls import path
from .views import RegisterView, registration_page

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("register_page/", registration_page, name="register_page")
]
