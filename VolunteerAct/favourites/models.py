from django.contrib.auth import get_user_model
from django.db import models

from VolunteerAct.categories.models import Event

AppUserModel = get_user_model()


class Favourites(models.Model):
    user = models.ForeignKey(
        to=AppUserModel,
        on_delete=models.CASCADE,
        related_name='user_favourites'
    )

    event = models.ForeignKey(
        to=Event,
        on_delete=models.CASCADE
    )

    class Meta:
        unique_together = ('user', 'event')
