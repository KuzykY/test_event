from django.contrib import admin
from .models import EventModel, EventTypeModel

admin.site.register(EventTypeModel)


@admin.register(EventModel)
class EventAdmin(admin.ModelAdmin):
    list_filter = ('timestamp', 'event_type')
