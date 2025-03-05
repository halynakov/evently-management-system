from django.shortcuts import render

# Create your views here.
def index(request):
  return render(request, "frontend/index.html")

def events(request):
  return render(request, "frontend/events.html")

def home(request):
  return render(request, "frontend/home.html")

def logup(request):
  return render(request, "frontend/forms/sign-up.html")

def login(request):
  return render(request, "frontend/forms/log-in.html")

def adminAddPost(request):
  return render(request, "frontend/forms/adminAddPost.html")

def adminChengePost(request):
  return render(request, "frontend/forms/adminChangePost.html")
