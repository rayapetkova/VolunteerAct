from django.shortcuts import render
from django.utils import timezone
from django.views.generic import DetailView

from VolunteerAct.categories.models import Category, Event


class CategoryDetailsView(DetailView):
    model = Category
    template_name = 'categories/category_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        upcoming_events = self.object.category_events.filter(time__gt=timezone.now())
        past_events = self.object.category_events.filter(time__lt=timezone.now())

        context['upcoming_events'] = upcoming_events
        context['past_events'] = past_events

        return context


class EventDetailsView(DetailView):
    model = Event
    template_name = 'categories/event_page.html'
