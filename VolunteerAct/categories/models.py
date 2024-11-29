from django.contrib.auth import get_user_model
from django.core import validators
from django.db import models
from django.db.models import ImageField

from VolunteerAct.app_users.models import AppUser
from cloudinary.models import CloudinaryField


AppUserModel = get_user_model()


class Category(models.Model):
    image = CloudinaryField('image')

    poster_img = CloudinaryField('image')

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

    def __str__(self):
        return self.name


class CategoryImages(models.Model):
    image = CloudinaryField('image')

    category = models.ForeignKey(
        to=Category,
        on_delete=models.CASCADE
    )

    author = models.ForeignKey(
        to=AppUser,
        on_delete=models.CASCADE
    )


class Event(models.Model):
    poster_image = CloudinaryField('image')

    title = models.CharField(
        max_length=70,
        null=False,
        blank=False,
        validators=[
            validators.MinLengthValidator(2, message="Title needs to be at least 2 characters long.")
        ]
    )

    details = models.CharField(
        max_length=10000,
        null=False,
        blank=False,
        validators=[
            validators.MinLengthValidator(1000, message="Details about the event need to be at least 150 characters long.")
        ]
    )

    online = models.BooleanField()

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

    online_meeting_link = models.URLField(
        max_length=200,
        null=False,
        blank=False
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

    def exact_location(self):
        if self.city != 'online_event' and self.location != 'online_event':
            return f"{self.location}, {self.city}"

        return 'Online'
