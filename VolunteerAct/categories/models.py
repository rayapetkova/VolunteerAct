from django.contrib.auth import get_user_model
from django.core import validators
from django.db import models

from VolunteerAct.app_users.models import AppUser


AppUserModel = get_user_model()


class Category(models.Model):
    name = models.CharField(
        max_length=30,
        unique=True,
        null=False,
        blank=False,
        validators=[
            validators.MinLengthValidator(3, message="Category name needs to be at least 3 characters long.")
        ]
    )

    short_description = models.CharField(
        max_length=250,
        null=False,
        blank=False,
        validators=[
            validators.MinLengthValidator(10, message="Category's short description needs to be at least 10 characters long.")
        ]
    )

    long_description = models.CharField(
        max_length=1100,
        null=False,
        blank=False,
        validators=[
            validators.MinLengthValidator(450, message="Category's long description needs to be at least 70 characters long.")
        ]
    )

    active_members = models.ManyToManyField(
        to=AppUserModel,
        related_name='categories'
    )


class Event(models.Model):
    title = models.CharField(
        max_length=70,
        null=False,
        blank=False,
        validators=[
            validators.MinLengthValidator(2, message="Title needs to be at lest 2 characters long.")
        ]
    )

    details = models.CharField(
        max_length=10000,
        null=False,
        blank=False,
        validators=[
            validators.MinLengthValidator(150, message="Details about the event need to be at least 150 characters long.")
        ]
    )

    city = models.CharField(
        max_length=50,
        null=False,
        blank=False,
        validators=[
            validators.MinLengthValidator(2, message="City needs to be at least 2 characters long.")
        ]
    )

    location = models.CharField(
        max_length=150,
        null=False,
        blank=False,
        validators=[
            validators.MinLengthValidator(10, message="Exact location needs to be at least 10 characters long.")
        ]
    )

    time = models.DateTimeField(
        null=False,
        blank=False
    )

    host = models.ForeignKey(
        to=AppUserModel,
        on_delete=models.CASCADE,
        related_name='host_events'
    )

    category = models.ForeignKey(
        to=Category,
        on_delete=models.CASCADE,
        related_name='category_events'
    )

    attendees = models.ManyToManyField(
        to=AppUser,
        related_name='events'
    )
