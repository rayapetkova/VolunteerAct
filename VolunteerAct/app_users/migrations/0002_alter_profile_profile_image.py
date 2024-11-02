# Generated by Django 5.1.1 on 2024-10-28 10:09

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=cloudinary.models.CloudinaryField(blank=True, default='https://res.cloudinary.com/dzfgtuvut/image/upload/v1730109853/f8dzfu6y42zieoecf4ix.png', max_length=255, null=True, verbose_name='image'),
        ),
    ]