# Generated by Django 5.1.1 on 2024-12-08 23:19

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_users', '0007_alter_profile_first_name_alter_profile_last_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=cloudinary.models.CloudinaryField(blank=True, default='https://res.cloudinary.com/dzfgtuvut/image/upload/v1731968047/zqknwmkjcvtl1nes9vnh.png', max_length=255, null=True),
        ),
    ]