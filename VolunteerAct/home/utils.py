from VolunteerAct.categories.models import Event


def get_emergency_events():
    return Event.objects.filter(is_emergency=True)
