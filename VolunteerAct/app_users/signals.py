from django.contrib.auth.models import Group
from django.db.models.signals import post_save
from django.dispatch import receiver
from VolunteerAct.app_users.tasks import send_email_to_new_registered_user

from VolunteerAct.app_users.models import AppUser, Profile


@receiver(post_save, sender=AppUser)
def create_profile(sender, instance, created, **kwargs):  # if created is True that means that the instance is new (the user registers)
    if created:
        profile = Profile(
            user=instance
        )

        profile.save()

        group = Group.objects.filter(name='regular_users').first()
        instance.groups.add(group)

        send_email_to_new_registered_user.delay(instance.email, profile.full_name())
