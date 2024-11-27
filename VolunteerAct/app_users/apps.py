from django.apps import AppConfig


class AppUsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'VolunteerAct.app_users'

    def ready(self):
        import VolunteerAct.app_users.signals
