from django.shortcuts import render
from events.models import Event, EventCategory
from datetime import datetime
import logging
logging.basicConfig(level=logging.INFO)

# Create your views here.
def index(request):
  events = Event.objects.all()
  eventCategoris = EventCategory.objects.all()
  
  return render(request, "frontend/index.html", {
    'events': events,
    'eventCategoris': eventCategoris
    })

def events(request):
  events = Event.objects.all()
  eventCategoris = EventCategory.objects.all()
  
  return render(request, "frontend/events.html", {
    'events': events,
    'eventCategoris': eventCategoris
    })

def home(request):
  eventCategoris = EventCategory.objects.all()
  
  return render(request, "frontend/home.html", {
    'eventCategoris': eventCategoris
    })

def signup(request):
  return render(request, "frontend/forms/sign-up.html")

def login(request):
  return render(request, "frontend/forms/log-in.html")

def adminAddPost(request):
  return render(request, "frontend/forms/adminAddPost.html")

def adminChengePost(request):
  return render(request, "frontend/forms/adminChangePost.html")
