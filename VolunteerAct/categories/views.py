from django.contrib.auth.mixins import UserPassesTestMixin
from django.core.exceptions import PermissionDenied
from django.db.models import Count, QuerySet
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import DetailView, UpdateView, DeleteView
from django.utils import timezone
from rest_framework.generics import UpdateAPIView, RetrieveUpdateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from VolunteerAct.categories.forms import EventForm, FilterForm, EventEditForm, EventDeleteForm
from VolunteerAct.categories.models import Category, Event
from VolunteerAct.categories.serializers import EventSerializer
from VolunteerAct.categories.utils import count_events, extract_keywords
from VolunteerAct.favourites.models import Favourites


def category_details(request, pk):
    event_form = EventForm(request.POST or None, request.FILES or None)

    category = Category.objects.get(pk=pk)
    upcoming_events = category.category_events.filter(time__gte=timezone.now()).order_by('time')
    past_events = category.category_events.filter(time__lt=timezone.now()).order_by('time')

    if request.user.is_authenticated:
        for u_event in upcoming_events:
            saved_to_favourites_by_logged_in_user = Favourites.objects.all().filter(user=request.user, event=u_event).first()

            if saved_to_favourites_by_logged_in_user:
                u_event.saved_to_favourites_by_logged_in_user = True
            else:
                u_event.saved_to_favourites_by_logged_in_user = False

    if request.user.is_authenticated:
        for p_event in past_events:
            saved_to_favourites_by_logged_in_user = Favourites.objects.all().filter(user=request.user, event=p_event).first()

            if saved_to_favourites_by_logged_in_user:
                p_event.saved_to_favourites_by_logged_in_user = True
            else:
                p_event.saved_to_favourites_by_logged_in_user = False

    members_upcoming_events = [event.attendees.all() for event in upcoming_events]
    if members_upcoming_events:
        members_upcoming_events = list(members_upcoming_events[0])  # get the queryset inside a list

    members_past_events = [event.attendees.all() for event in past_events]
    if members_past_events:
        members_past_events = list(members_past_events[0])

    active_members = members_upcoming_events + members_past_events

    if request.method == "POST":
        if event_form.is_valid():
            event = event_form.save(commit=False)
            event.host = request.user
            event.category = category

            event.save()

            event.attendees.add(request.user)
            return redirect('category-page', pk=pk)

    context = {
        'category': category,
        'event_form': event_form,
        'upcoming_events': upcoming_events[:2],
        'past_events': past_events[:2],
        'count_upcoming_events': count_events(len(upcoming_events), 2),
        'count_past_events': count_events(len(past_events), 2),
        'active_members': active_members[:36]
    }

    return render(request, 'categories/category_page.html', context=context)


def all_events_view(request):
    filter_form = FilterForm(request.GET or None)

    all_events = Event.objects.all().order_by('-time')

    for event in all_events:
        event.already_passed = True if event.time < timezone.now() else False

        saved_to_favourites_by_logged_in_user = Favourites.objects.all().filter(user=request.user, event=event).first()

        if saved_to_favourites_by_logged_in_user:
            event.saved_to_favourites_by_logged_in_user = True
        else:
            event.saved_to_favourites_by_logged_in_user = False

    if request.method == "GET":
        if filter_form.is_valid():
            categories_filter = request.GET.getlist('category')
            cities_filter = request.GET.getlist('city')
            time_filter = request.GET.getlist('time')

            if categories_filter:
                all_events = all_events.filter(category__name__in=categories_filter)

            if cities_filter:
                all_events = all_events.filter(city__in=cities_filter)

            if len(time_filter) == 1:
                if 'Past' in time_filter:
                    all_events = all_events.filter(time__lt=timezone.now())

                if 'Upcoming' in time_filter:
                    all_events = all_events.filter(time__gte=timezone.now())

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

        see_more_events = Event.objects.all().filter(
            category__id=self.object.category.id,
            time__gte=timezone.now(),
        ).exclude(id=self.object.id)[:4]
        context['see_more_events'] = see_more_events
        context['count_more_events'] = count_events(len(see_more_events), 4)

        details_keywords = extract_keywords(self.object.details)
        context['keywords'] = details_keywords

        comments = self.object.comments.all().order_by('-created_at')
        context['event_comments'] = comments[:3]
        context['count_comments'] = count_events(len(comments), 3)

        if self.request.user.is_authenticated:
            user_favourite_event = Favourites.objects.filter(user=self.request.user, event=self.object)
            context['user_favourite_event'] = user_favourite_event

        self.object.passed_event = True if self.object.time < timezone.now() else False

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


class EventUpdateView(UserPassesTestMixin, UpdateView):
    model = Event
    form_class = EventEditForm
    template_name = 'categories/edit_event_page.html'

    def test_func(self):
        if self.get_object().host != self.request.user:
            return False

        return True

    def handle_no_permission(self):
        raise PermissionDenied()

    def get_success_url(self):
        return reverse_lazy('event-page', kwargs={
            'categoryId': self.object.category.id,
            'pk': self.object.id
        })


class EventListAPIView(APIView):

    def get(self, request):
        searched_title = request.GET['searchedTitle']
        events = Event.objects.filter(title__icontains=searched_title)
        serializer = EventSerializer(events, many=True)
        json_data = serializer.data

        return Response(data=json_data)


class EventUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
