import uuid

from django.db import models


class EventTypeModel(models.Model):
    class Meta:
        db_table = 'event_type'

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class EventModel(models.Model):
    class Meta:
        db_table = 'event'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    # user = models.ForeignKey('UserModel')
    event_type = models.ForeignKey(EventTypeModel, null=True, on_delete=models.SET_NULL, related_name='event_type')
    info = models.JSONField()
    timestamp = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.info
