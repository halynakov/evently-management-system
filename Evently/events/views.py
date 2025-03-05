from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from events.models import Event, EventUser, EventCategory
from events.serializers import EventSerializer, EventCreateSerializer

def index(request):
    """Главная страница с событиями"""
    events_by_category = {  
        category.name: list(category.event_set.all()) 
        for category in EventCategory.objects.all()
    }

    return render(request, "frontend/index.html", {"events_by_category": events_by_category})

class EventViewSet(viewsets.ViewSet):
    """API для работы с событиями"""

    def list(self, request):
        """GET /api/events/ - Получить все события"""
        events = Event.objects.all()
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'], url_path='user')
    def user_events(self, request):
        """GET /api/events/user/ - Получить события текущего пользователя"""
        user_id = request.GET.get("user_id")
        if not user_id:
            return Response({"error": "user_id is required"}, status=400)
        user_events = Event.objects.filter(eventuser__user_id=user_id)
        serializer = EventSerializer(user_events, many=True)
        return Response(serializer.data)

    def create(self, request):
        """POST /api/events/ - Создать событие"""
        serializer = EventCreateSerializer(data=request.data)
        if serializer.is_valid():
            event = serializer.save()
            return Response(EventSerializer(event).data, status=201)
        return Response(serializer.errors, status=400)
    
    @action(detail=False, methods=['post'], url_path='approve')
    def approve_event(self, request):
        """ POST /api/events/approve/ - Approve an event for a user (set is_approved=True)
        """
        user_id = request.GET.get("user_id")
        event_id = request.GET.get("event_id")

        if not user_id or not event_id:
            return Response({"error": "user_id and event_id are required"})

        try:
            event_user = EventUser.objects.get(user_id=user_id, event_id=event_id)
            event_user.is_approved = True
            event_user.save()
            return Response({"message": "Event approved successfully"}, status=200)
        except EventUser.DoesNotExist:
            return Response({"error": "User is not registered for this event"}, status=404)