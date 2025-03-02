from django.db import models
from django.conf import settings  

class EventCategory(models.Model):
    """Категории событий"""
    name = models.CharField(max_length=255, unique=True)  
    def __str__(self):
        return self.name

class Event(models.Model):
    """Таблица событий"""
    name = models.CharField(max_length=255)
    date = models.DateTimeField()
    location = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    category = models.ForeignKey(
        EventCategory,
        on_delete=models.PROTECT,   
        null=False,
        blank=False
    )

    def __str__(self):
        return self.name


class EventUser(models.Model):
    """Таблица связи пользователей с событиями"""
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    registered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.email} -> {self.event.name}"
