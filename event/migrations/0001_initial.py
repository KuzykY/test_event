# Generated by Django 4.1.6 on 2023-02-06 13:19

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EventTypeModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=256)),
            ],
            options={
                'db_table': 'event_type',
            },
        ),
        migrations.CreateModel(
            name='EventModel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('info', models.JSONField()),
                ('timestamp', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('event_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event_type', to='event.eventtypemodel')),
            ],
            options={
                'db_table': 'event',
            },
        ),
    ]
