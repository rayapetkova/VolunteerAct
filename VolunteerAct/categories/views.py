from django.db.models import Count
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import DetailView, UpdateView, DeleteView
from django.utils import timezone

from VolunteerAct.categories.forms import EventForm, FilterForm, EventEditForm, EventDeleteForm
from VolunteerAct.categories.models import Category, Event
from VolunteerAct.categories.utils import count_events, extract_keywords


def category_details(request, pk):
    event_form = EventForm(request.POST or None, request.FILES or None)

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
        'count_upcoming_events': count_events(len(upcoming_events), 2),
        'count_past_events': count_events(len(past_events), 2)
    }

    return render(request, 'categories/category_page.html', context=context)


def all_events_view(request):
    filter_form = FilterForm(request.GET or None)

    all_events = Event.objects.all()

    if request.method == "GET":
        if filter_form.is_valid():
            categories_filter = request.GET.getlist('category')
            cities_filter = request.GET.getlist('city')

            if categories_filter:
                all_events = all_events.filter(category__name__in=categories_filter)

            if cities_filter:
                all_events = all_events.filter(city__in=cities_filter)

    context = {
        'filter_form': filter_form,
        'all_events': all_events
    }

    return render(request, 'categories/all_events_page.html', context=context)


class EventDetailsView(DetailView, DeleteView):
    model = Event
    template_name = 'categories/event_page.html'
    form_class = EventDeleteForm
    success_url = reverse_lazy('home-page')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        see_more_events = Event.objects.all().filter(category__id=self.object.category.id, time__gte=timezone.now())[:4]
        context['see_more_events'] = see_more_events
        context['count_more_events'] = count_events(len(see_more_events), 4)

        details_keywords = extract_keywords(self.object.details)
        context['keywords'] = details_keywords

        return context

    # Override form_invalid method because when performing POST, Django checks if the form is valid and calls
    # the form_valid method. But our form is not valid and we call form_valid in form_invalid method
    def form_invalid(self, form):
        return self.form_valid(form)

    # This is another way
    # def post(self, request, *args, **kwargs):
    #     self.object = self.get_object()
    #     form = self.get_form()
    #     return self.form_valid(form=form)


class EventUpdateView(UpdateView):
    model = Event
    form_class = EventEditForm
    template_name = 'categories/edit_event_page.html'

    def get_success_url(self):
        return reverse_lazy('event-page', kwargs={
            'categoryId': self.object.category.id,
            'pk': self.object.id
        })
