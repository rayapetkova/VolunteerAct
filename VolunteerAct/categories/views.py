from django.shortcuts import render, redirect
from django.utils import timezone
from django.views.generic import DetailView

from VolunteerAct.categories.forms import EventForm
from VolunteerAct.categories.models import Category, Event
from VolunteerAct.categories.utils import count_events


def category_details(request, pk):
    event_form = EventForm(request.POST or None, request.FILES or None)
    print(request.FILES)
    category = Category.objects.get(pk=pk)
    upcoming_events = category.category_events.filter(time__gte=timezone.now()).order_by('time')
    past_events = category.category_events.filter(time__lt=timezone.now()).order_by('time')

    if request.method == "POST":
        if event_form.is_valid():
            event = event_form.save(commit=False)
            event.host = request.user
            event.category = category

            event.save()
            return redirect('category-page', pk=pk)

    context = {
        'category': category,
        'event_form': event_form,
        'upcoming_events': upcoming_events[:2],
        'past_events': past_events[:2],
        'count_upcoming_events': count_events(len(upcoming_events)),
        'count_past_events': count_events(len(past_events))
    }

    return render(request, 'categories/category_page.html', context=context)


class EventDetailsView(DetailView):
    model = Event
    template_name = 'categories/event_page.html'
