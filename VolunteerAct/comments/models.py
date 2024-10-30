from django.core import validators
from django.db import models

from VolunteerAct.categories.models import Event


class Comment(models.Model):
    body = models.TextField(
        null=False,
        blank=False,
        max_length=500,
        validators=[
            validators.MinLengthValidator(10, message='Comment needs to be at least 10 characters.')
        ]
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    event = models.ForeignKey(
        to=Event,
        on_delete=models.CASCADE
    )
