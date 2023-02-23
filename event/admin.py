from django.contrib import admin
from .models import Event, EventType

admin.site.register(EventType)


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_filter = ('timestamp', 'event_type')
