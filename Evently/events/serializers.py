from rest_framework import serializers
from events.models import Event
from events.models import Event, EventCategory

class EventSerializer(serializers.ModelSerializer):
    """Сериализатор для получения событий"""

    category_name = serializers.CharField(source='category.name', read_only=True)

    class Meta:
        model = Event
        fields = ['id', 'name', 'date', 'location', 'description', 'category', 'category_name']

class EventCreateSerializer(serializers.ModelSerializer):
    """Сериализатор для создания события"""

    category = serializers.PrimaryKeyRelatedField(queryset=EventCategory.objects.all())

    class Meta:
        model = Event
        fields = ['name', 'date', 'location', 'description', 'category']


