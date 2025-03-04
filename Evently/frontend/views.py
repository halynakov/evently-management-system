from django.shortcuts import render

# Create your views here.
def index(request):
  return render(request, "frontend/index.html")

def events(request):
  return render(request, "frontend/events.html")

def home(request):
  return render(request, "frontend/home.html")