# Generated by Django 5.1.1 on 2024-10-12 14:41

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
            field=models.CharField(blank=True, max_length=10, null=True, validators=[django.core.validators.MinLengthValidator(10, message='Phone number needs to be exact 10 characters long.')]),
        ),
    ]
