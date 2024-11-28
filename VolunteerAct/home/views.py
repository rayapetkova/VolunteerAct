from django.shortcuts import render, redirect

from VolunteerAct.categories.models import Category, Event
from django.utils import timezone

from VolunteerAct.categories.utils import get_cities

from decouple import config

from VolunteerAct.favourites.models import Favourites
from VolunteerAct.home.forms import ContactUsForm


def home_page(request):
    popular_cities = [city[0] for city in get_cities() if city[0] != 'online_event']
    pixabay_api_url = config('PIXABAY_API_URL')
    upcoming_events = Event.objects.filter(time__gte=timezone.now()).order_by('time')[:4]

    if request.user.is_authenticated:
        for event in upcoming_events:
            saved_to_favourites_by_logged_in_user = Favourites.objects.all().filter(user=request.user, event=event).first()

            if saved_to_favourites_by_logged_in_user:
                event.saved_to_favourites_by_logged_in_user = True
            else:
                event.saved_to_favourites_by_logged_in_user = False

    context = {
        'categories': Category.objects.order_by('id').all(),
        'upcoming_events': upcoming_events,
        'popular_cities': popular_cities[:6],
        'pixabay_api_url': pixabay_api_url
    }

    return render(request, "home/home_page.html", context=context)


def contact_us_page(request):
    form = ContactUsForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            return redirect('contact-us')

    context = {
        'form': form
    }

    return render(request, 'home/contact_us_page.html', context=context)
