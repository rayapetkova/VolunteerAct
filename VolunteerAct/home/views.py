from django.shortcuts import render

from VolunteerAct.categories.models import Category, Event
from django.utils import timezone

from VolunteerAct.categories.utils import get_cities

from decouple import config


def home_page(request):
    popular_cities = [city[0] for city in get_cities()]
    pixabay_api_url = config('PIXABAY_API_URL')

    context = {
        'categories': Category.objects.order_by('id').all(),
        'upcoming_events': Event.objects.filter(time__gte=timezone.now()).order_by('time')[:4],
        'popular_cities': popular_cities,
        'pixabay_api_url': pixabay_api_url
    }

    return render(request, "home/home_page.html", context=context)