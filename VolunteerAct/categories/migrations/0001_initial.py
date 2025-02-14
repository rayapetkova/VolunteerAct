# Generated by Django 5.1.1 on 2024-10-26 11:05

import cloudinary.models
import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('poster_img', cloudinary.models.CloudinaryField(max_length=255, null=True, verbose_name='image')),
                ('name', models.CharField(max_length=30, unique=True, validators=[django.core.validators.MinLengthValidator(3, message='Category name needs to be at least 3 characters long.')])),
                ('short_description', models.CharField(max_length=250, validators=[django.core.validators.MinLengthValidator(10, message="Category's short description needs to be at least 10 characters long.")])),
                ('long_description', models.CharField(max_length=1100, validators=[django.core.validators.MinLengthValidator(450, message="Category's long description needs to be at least 70 characters long.")])),
                ('active_members', models.ManyToManyField(related_name='categories', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poster_image', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('title', models.CharField(max_length=70, validators=[django.core.validators.MinLengthValidator(2, message='Title needs to be at least 2 characters long.')])),
                ('details', models.CharField(max_length=10000, validators=[django.core.validators.MinLengthValidator(1000, message='Details about the event need to be at least 150 characters long.')])),
                ('city', models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(2, message='City needs to be at least 2 characters long.')])),
                ('location', models.CharField(max_length=150, validators=[django.core.validators.MinLengthValidator(10, message='Exact location needs to be at least 10 characters long.')])),
                ('time', models.DateTimeField()),
                ('attendees', models.ManyToManyField(related_name='events', to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category_events', to='categories.category')),
                ('host', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='host_events', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
