from decouple import config
from django.shortcuts import render
from django.utils import timezone
import requests

from VolunteerAct.categories.models import Event
from VolunteerAct.categories.utils import count_events
from VolunteerAct.home.utils import get_emergency_events


def city_details_view(request, city_name):
    upcoming_events = Event.objects.filter(city=city_name, time__gte=timezone.now()).order_by('-time')[:3]
    past_events = Event.objects.filter(city=city_name, time__lt=timezone.now()).order_by('time')[:3]
    pixabay_api_url = f"{config('PIXABAY_API_URL')}&q={city_name}"
    response_city_picture = requests.get(pixabay_api_url)
    city_picture = response_city_picture.json()['hits'][0]['webformatURL']

    context = {
        'city_name': city_name,
        'city_picture': city_picture,
        'upcoming_events': upcoming_events,
        'past_events': past_events,
        'count_upcoming_events': count_events(len(upcoming_events), 2),
        'count_past_events': count_events(len(past_events), 2),
        'emergency_events': get_emergency_events()
    }

    return render(request, 'cities/city.html', context=context)
