from celery import shared_task
from django.core.mail import send_mail
from django.utils.timezone import now
from datetime import timedelta
from events.models import EventUser

@shared_task
def send_event_reminder(event_user_id):
    try:
        event_user = EventUser.objects.get(id=event_user_id)
    except EventUser.DoesNotExist:
        return  

    event = event_user.event
    user_email = event_user.user.email

    subject = f"Нагадування: {event.name}"
    message = f"Привіт! Нагадуємо, що подія '{event.name}' розпочнеться {event.date} у {event.location}."

    send_mail(subject, message, "noreply@evently.com", [user_email])
    print(f"Отправлено напоминание на {user_email} про {event.name}")


