from django.shortcuts import render

# Create your views here.
from django.core.mail import send_mail
from rest_framework.response import Response
from rest_framework import status, generics
from .models import CustomUser
from .serializers import RegistrationSerializer
from django.conf import settings


class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegistrationSerializer

    def perform_create(self, serializer):
        user = serializer.save()
        verification_link = f"http://127.0.0.1:8000/verify/{user.verification_token}/"

        send_mail(
            "Подтверждение регистрации",
            f"Пройдите по ссылке для подтверждения: {verification_link}",
            settings.EMAIL_HOST_USER,
            [user.email],
            fail_silently=False,
        )

        return Response(
            {"message": "Письмо с подтверждением отправлено!"},
            status=status.HTTP_201_CREATED,
        )


def registration_page(request):
    return render(request, "verification/register.html")
	
def home(request):
    return HttpResponse("Welcome to Evently!")
