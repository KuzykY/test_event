from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Event, EventType


class EventSerializer(ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'


# class CreateEventSerializer(serializers.Serializer):
#     event_type = serializers.CharField()
#     info = serializers.JSONField()
#     timestamp = serializers.DateTimeField()


class EventTypeSerializer(ModelSerializer):
    class Meta:
        model = EventType
        fields = '__all__'
