from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models

from VolunteerAct.app_users.managers import AppUserManager


class AppUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        unique=True,
        null=False,
        blank=False
    )

    USERNAME_FIELD = 'email'
    objects = AppUserManager()

