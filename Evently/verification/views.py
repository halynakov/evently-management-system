from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login  # Добавьте logout здесь
from django.core.mail import send_mail
from rest_framework.response import Response
from rest_framework import status, generics
from .models import CustomUser
from .serializers import RegistrationSerializer
from django.conf import settings
from .forms import LoginForm
from django.http import HttpResponse  # Не забудьте импортировать HttpResponse


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

        # return Response(
        #     {"message": "Письмо с подтверждением отправлено!"},
        #     status=status.HTTP_201_CREATED,
        # )


def registration_page(request):
    return render(request, "verification/register.html")

def verify_user(request, token):
    """Обрабатывает верификацию пользователя по токену"""
    try:
        user = CustomUser.objects.get(verification_token=token)
        if user.is_verified:
            return HttpResponse("Аккаунт уже подтверждён!")
        user.is_verified = True
        user.save()
        return HttpResponse("Аккаунт успешно подтверждён!")
    except CustomUser.DoesNotExist:
        return HttpResponse("Неверный токен!", status=400)


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(email=email, password=password)
            print(f"Попытка входа пользователя: {email}")  
            if user is not None:
                login(request, user)
                print("Авторизация успешна!")  
                return redirect('/', {"user_id": user.id})
  
            else:
                print("Ошибка: неверный email или пароль.")  
                form.add_error(None, "Неверный email или пароль.")
    else:
        form = LoginForm()
    return render(request, "verification/login.html", {'form': form})

# def logout_view(request):
#     """Обрабатывает выход пользователя"""
#     logout(request)
#     return redirect("login")
