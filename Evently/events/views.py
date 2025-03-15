from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from verification.models import CustomUser
from events.models import Event, EventUser, EventCategory
from events.serializers import EventSerializer, EventCreateSerializer
from datetime import timedelta 
from django.utils.timezone import localtime, now
from events.utils import send_event_email, schedule_email

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
        """Пользователь подтверждает участие в событии"""
        user_id = request.GET.get("user_id")
        event_id = request.GET.get("event_id")

        if not user_id or not event_id:
            return Response({"error": "user_id и event_id обязательны"}, status=400)

        try:
            event_user = EventUser.objects.get(user_id=user_id, event_id=event_id)
            event = event_user.event

            event_user.is_approved = True
            event_user.save()

            time_until_event = event.date - now()

            if time_until_event > timedelta(hours=24):
                schedule_email(event_user, 24)  # Запланировать email за 24 часа до события

            if time_until_event > timedelta(hours=1):
                schedule_email(event_user, 1)  # Запланировать email за 1 час до события
            else:
                send_event_email(event_user)  # Если осталось менее часа → отправляем СРАЗУ

            return Response({"message": "Участие подтверждено, напоминания запланированы"}, status=200)

        except EventUser.DoesNotExist:
            return Response({"error": "Пользователь не зарегистрирован на это событие"}, status=404)
        
    @action(detail=False, methods=['post'], url_path='apply')
    def apply_for_event(self, request):
        """ POST /api/events/apply/ - Register a user for an event """
        user_id = request.GET.get("user_id")
        event_id = request.GET.get("event_id")

        if not user_id or not event_id:
            return Response({"error": "user_id and event_id are required"}, status=400)

        try:
            user = CustomUser.objects.get(id=user_id)
            event = Event.objects.get(id=event_id)
        except CustomUser.DoesNotExist:
            return Response({"error": "User not found"}, status=404)
        except Event.DoesNotExist:
            return Response({"error": "Event not found"}, status=404)

        if EventUser.objects.filter(user=user, event=event).exists():
            return Response({"error": "User is already registered for this event"}, status=400)

        event_user = EventUser.objects.create(
            user=user,
            event=event,
            is_approved=False
        )

        return Response({
            "message": "User successfully applied for the event",
            "event_id": event_user.event.id,
            "user_id": event_user.user.id,
            "registered_at": event_user.registered_at,
            "is_approved": event_user.is_approved
        }, status=201)

    def update(self, request, pk=None):
        """PUT /api/events/<id>/ - Update an existing event"""
        event = get_object_or_404(Event, pk=pk)
        serializer = EventCreateSerializer(event, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        """DELETE /api/events/<id>/ - Delete an event"""
        event = get_object_or_404(Event, pk=pk)
        event.delete()
        return Response({"message": "Event deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
