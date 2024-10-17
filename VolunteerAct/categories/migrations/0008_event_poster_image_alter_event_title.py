# Generated by Django 5.1.1 on 2024-10-10 14:51

import cloudinary.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0007_alter_category_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='poster_image',
            field=cloudinary.models.CloudinaryField(max_length=255, null=True, verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='event',
            name='title',
            field=models.CharField(max_length=70, validators=[django.core.validators.MinLengthValidator(2, message='Title needs to be at least 2 characters long.')]),
        ),
    ]