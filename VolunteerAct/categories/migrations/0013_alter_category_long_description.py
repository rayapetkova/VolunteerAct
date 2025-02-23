# Generated by Django 5.1.1 on 2025-02-23 09:35

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0012_alter_event_is_emergency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='long_description',
            field=models.CharField(max_length=500, validators=[django.core.validators.MinLengthValidator(50, message="Category's long description needs to be at least 50 characters long.")]),
        ),
    ]
