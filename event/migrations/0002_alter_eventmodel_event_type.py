# Generated by Django 4.1.6 on 2023-02-06 15:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventmodel',
            name='event_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='event_type', to='event.eventtypemodel'),
        ),
    ]
