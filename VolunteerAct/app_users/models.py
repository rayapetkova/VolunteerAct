from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
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

