from cloudinary.models import CloudinaryField
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.core import validators
from django.db import models

from VolunteerAct.app_users.managers import AppUserManager
from django.utils.translation import gettext_lazy as _

from decouple import config

from VolunteerAct.app_users.validators import first_name_validator, last_name_validator, phone_number_validator


class AppUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        unique=True,
        null=False,
        blank=False,
        error_messages={
            'unique': "User with this email already exists."
        }
    )

    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )

    USERNAME_FIELD = 'email'
    objects = AppUserManager()


class Profile(models.Model):
    profile_image = CloudinaryField(
        resource_type='image',
        default=config('DEFAULT_PROFILE_IMAGE'),
        null=True,
        blank=True
    )

    first_name = models.CharField(
        max_length=150,
        null=True,
        blank=False,
        validators=[
            validators.MinLengthValidator(2, message="First name needs to be at least 2 characters long."),
            first_name_validator
        ],
    )

    last_name = models.CharField(
        max_length=150,
        null=True,
        blank=False,
        validators=[
            validators.MinLengthValidator(2, message="Last name needs to be at least 2 characters long."),
            last_name_validator
        ]
    )

    phone_number = models.CharField(
        max_length=10,
        null=True,
        blank=True,
        validators=[
            validators.MinLengthValidator(10, message="Phone number needs to be exactly 10 characters long."),
            phone_number_validator
        ]
    )

    bio = models.TextField(
        max_length=800,
        null=True,
        blank=True,
        validators=[
            validators.MinLengthValidator(10, message="Bio needs to be at least 10 characters long.")
        ]
    )

    user = models.OneToOneField(
        to=AppUser,
        on_delete=models.CASCADE,
        related_name='profile'
    )

    def full_name(self):
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        elif self.first_name and not self.last_name:
            return self.first_name
        elif not self.first_name and self.last_name:
            return self.last_name

        return self.user.email
