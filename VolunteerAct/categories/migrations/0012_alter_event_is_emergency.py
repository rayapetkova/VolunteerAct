# Generated by Django 5.1.1 on 2024-11-30 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0011_event_is_emergency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='is_emergency',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]