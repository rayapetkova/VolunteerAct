from django.core import validators
from django.db import models

from VolunteerAct.app_users.models import AppUser


class Category(models.Model):
    name = models.CharField(
        max_length=30,
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
            validators.MinLengthValidator(70, message="Category's long description needs to be at least 70 characters long.")
        ]
    )

    active_members = models.ManyToManyField(
        to=AppUser,
        related_name='categories'
    )