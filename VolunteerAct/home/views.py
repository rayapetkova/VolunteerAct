from django.shortcuts import render

from VolunteerAct.categories.models import Category, Event
from django.utils import timezone


def home_page(request):
    context = {
        'categories': Category.objects.order_by('id').all(),
        'upcoming_events': Event.objects.filter(time__gte=timezone.now()).order_by('time')[:4]
    }

    return render(request, "home/home_page.html", context=context)