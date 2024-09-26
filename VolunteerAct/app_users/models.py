from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.core import validators
from django.db import models

from VolunteerAct.app_users.managers import AppUserManager
from django.utils.translation import gettext_lazy as _


class AppUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        unique=True,
        null=False,
        blank=False
    )

    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )

    USERNAME_FIELD = 'email'
    objects = AppUserManager()


class Profile(models.Model):
    first_name = models.CharField(
        max_length=150,
        null=False,
        blank=False,
        validators=[
            validators.MinLengthValidator(2, message="First name needs to be at least 2 characters long.")
        ]
    )

    last_name = models.CharField(
        max_length=150,
        null=False,
        blank=False,
        validators=[
            validators.MinLengthValidator(2, message="Last name needs to be at least 2 characters long.")
        ]
    )

    phone_number = models.CharField(
        max_length=10,
        null=True,
        blank=True,
        validators=[
            validators.MinLengthValidator(2, message="Phone number needs to be exact 10 characters long.")
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