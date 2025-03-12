from django.shortcuts import render
from events.models import Event, EventCategory, EventUser

# Create your views here.
def index(request):
  events = Event.objects.all()
  eventCategoris = EventCategory.objects.all()

  locations = []
  for event in events:
    locations.append(event.location)
  uniqueLocations = list(set(locations))
  
  return render(request, "frontend/index.html", {
    'events': events,
    'eventCategoris': eventCategoris,
    'uniqueLocations': uniqueLocations
    })

def events(request):
  events = Event.objects.all()
  eventCategoris = EventCategory.objects.all()

  locations = []
  for event in events:
    locations.append(event.location)
  uniqueLocations = list(set(locations))
  
  return render(request, "frontend/events.html", {
    'events': events,
    'eventCategoris': eventCategoris,
    'uniqueLocations': uniqueLocations
    })

def home(request):
  events = Event.objects.all()
  eventCategoris = EventCategory.objects.all()
  eventsUser = EventUser.objects.all()

  locations = []
  for event in events:
    locations.append(event.location)
  uniqueLocations = list(set(locations))
  
  return render(request, "frontend/home.html", {
    'eventCategoris': eventCategoris,
    'uniqueLocations': uniqueLocations,
    'eventsUser': eventsUser
    })

def admin(request):
  events = Event.objects.all()
  eventCategoris = EventCategory.objects.all()

  locations = []
  for event in events:
    locations.append(event.location)
  uniqueLocations = list(set(locations))
  
  return render(request, "frontend/admin.html", {
    'events': events,
    'eventCategoris': eventCategoris,
    'uniqueLocations': uniqueLocations
    })

def signup(request):
  return render(request, "frontend/forms/sign-up.html")

def login(request):
  return render(request, "frontend/forms/log-in.html")

def adminAddPost(request):
  return render(request, "frontend/forms/adminAddPost.html")

def adminChengePost(request):
  return render(request, "frontend/forms/adminChangePost.html")
