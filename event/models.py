import uuid
from django.contrib.auth.models import User
from django.db import models


class EventType(models.Model):
    class Meta:
        db_table = 'event_type'

    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class Event(models.Model):
    class Meta:
        db_table = 'event'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event_type = models.ForeignKey(EventType, on_delete=models.CASCADE)
    info = models.JSONField()
    timestamp = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)
