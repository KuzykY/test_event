from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from event.models import EventType, Event
from event.serializers import EventSerializer


class CreateEventView(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = EventSerializer

    def create(self, request, *args, **kwargs):
        event_type_name = request.data.get('event_type', None)
        info = request.data.get('info', None)
        timestamp = request.data.get('timestamp', None)
        user = request.user

        # Якщо event_type, який приходить, немає в базі то створити його.
        event_type, _ = EventType.objects.get_or_create(name=event_type_name)

        # Зберегти подію
        event = Event.objects.create(
            user=user,
            event_type=event_type,
            info=info,
            timestamp=timestamp
        )
        serializer = self.get_serializer(event)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class EventListView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = EventSerializer
    queryset = Event.objects.all()
