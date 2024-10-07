from django.shortcuts import render
from django.utils import timezone
from django.views.generic import DetailView

from VolunteerAct.categories.forms import EventForm
from VolunteerAct.categories.models import Category, Event


def category_details(request, pk):
    event_form = EventForm(request.POST or None)
    category = Category.objects.get(pk=pk)
    upcoming_events = category.category_events.filter(time__gt=timezone.now())
    past_events = category.category_events.filter(time__lt=timezone.now())

    if request.method == "POST":
        if event_form.is_valid():
            event_form.save(commit=True)
            print(event_form.cleaned_data)
        else:
            print(event_form.errors)

    context = {
        'category': category,
        'event_form': event_form,
        'upcoming_events': upcoming_events,
        'past_events': past_events
    }

    return render(request, 'categories/category_page.html', context=context)


class EventDetailsView(DetailView):
    model = Event
    template_name = 'categories/event_page.html'
