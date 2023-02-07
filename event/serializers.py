from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import EventModel, EventTypeModel


class EventSerializer(ModelSerializer):
    class Meta:
        model = EventModel
        fields = ('event_type','info', 'timestamp')


class CreateEventSerializer(serializers.Serializer):
    event_type = serializers.CharField()
    info = serializers.JSONField()
    timestamp = serializers.DateTimeField()


class EventTypeSerializer(ModelSerializer):
    class Meta:
        model = EventTypeModel
        fields = ('name',)
