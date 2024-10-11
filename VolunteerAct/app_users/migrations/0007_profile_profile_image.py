# Generated by Django 5.1.1 on 2024-10-11 19:08

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_users', '0006_alter_profile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile_image',
            field=cloudinary.models.CloudinaryField(max_length=255, null=True, verbose_name='image'),
        ),
    ]
