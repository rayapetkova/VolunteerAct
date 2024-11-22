from django.shortcuts import render
from django.utils import timezone

from VolunteerAct.categories.models import Event
from VolunteerAct.categories.utils import count_events


def city_details_view(request, city_name):
    upcoming_events = Event.objects.filter(city=city_name, time__gte=timezone.now())
    past_events = Event.objects.filter(city=city_name, time__lt=timezone.now())

    context = {
        'city_name': city_name,
        'upcoming_events': upcoming_events,
        'past_events': past_events,
        'count_upcoming_events': count_events(len(upcoming_events), 2),
        'count_past_events': count_events(len(past_events), 2),
    }

    return render(request, 'cities/city.html', context=context)
