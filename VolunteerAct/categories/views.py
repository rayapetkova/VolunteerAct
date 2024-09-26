from django.shortcuts import render
from django.views.generic import DetailView

from VolunteerAct.categories.models import Category, Event


class CategoryDetailsView(DetailView):
    model = Category
    template_name = 'categories/category_page.html'


class EventDetailsView(DetailView):
    model = Event
    template_name = 'categories/event_page.html'
