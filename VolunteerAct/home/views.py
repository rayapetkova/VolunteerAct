from django.core.mail import send_mail
from django.shortcuts import render, redirect

from VolunteerAct.categories.models import Category, Event
from django.utils import timezone

from VolunteerAct.categories.utils import get_cities

from decouple import config
from django.conf import settings

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

    if request.user.is_authenticated:
        form.fields['full_name'].initial = f"{request.user.profile.first_name} {request.user.profile.last_name}"
        form.fields['email'].initial = request.user.email

    if request.method == 'POST':
        if form.is_valid():
            full_name = form.cleaned_data['full_name']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            from_email = form.cleaned_data['email']
            recipient_list = [settings.EMAIL_HOST_USER]

            message += f"\n\n\n\nSend by {full_name}, {from_email}"

            send_mail(
                subject=subject,
                message=message,
                from_email=from_email,
                recipient_list=recipient_list
            )

            return redirect('contact-us')

    context = {
        'form': form
    }

    return render(request, 'home/contact_us_page.html', context=context)
