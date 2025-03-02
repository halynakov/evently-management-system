from django.shortcuts import render
from events.models import Event, EventCategory

def index(request):
    """Главная страница с событиями"""
    events_by_category = {  
        category.name: list(category.event_set.all()) 
        for category in EventCategory.objects.all()
    }

    return render(request, "frontend/index.html", {"events_by_category": events_by_category})
