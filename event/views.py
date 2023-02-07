from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import EventTypeModel
from .serializers import EventSerializer, CreateEventSerializer


class EventView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = (IsAuthenticated,)

    def post(self, *args, **kwargs):
        data = self.request.data
        request_serializer = CreateEventSerializer(data=data)
        if not request_serializer.is_valid():
            return Response(request_serializer.errors, status.HTTP_400_BAD_REQUEST)
        event_type, created = EventTypeModel.objects.get_or_create(name=data['event_type'])
        event = {"event_type": event_type.id, "info": data['info'], "timestamp": data['timestamp']}
        serializer = EventSerializer(data=event)
        if not serializer.is_valid():
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)
