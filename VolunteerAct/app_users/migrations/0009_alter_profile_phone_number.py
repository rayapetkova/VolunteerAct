# Generated by Django 5.1.1 on 2024-12-11 00:03

import VolunteerAct.app_users.validators
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_users', '0008_alter_profile_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='phone_number',
            field=models.CharField(blank=True, max_length=10, null=True, validators=[django.core.validators.MinLengthValidator(10, message='Phone number needs to be exactly 10 characters long.'), VolunteerAct.app_users.validators.phone_number_validator]),
        ),
    ]