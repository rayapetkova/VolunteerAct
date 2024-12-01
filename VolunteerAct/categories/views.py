from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import UserPassesTestMixin
from django.core.exceptions import PermissionDenied
from django.core.mail import send_mail
from django.db.models import Count, QuerySet
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.utils import timezone
from django.utils.html import strip_tags
from django.views.generic import DetailView, UpdateView, DeleteView, CreateView
from django.utils import timezone
from rest_framework import status
from rest_framework.generics import UpdateAPIView, RetrieveUpdateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from VolunteerAct.categories.forms import EventForm, FilterForm, EventEditForm, EventDeleteForm, CategoryImagesForm
from VolunteerAct.categories.models import Category, Event, CategoryImages
from VolunteerAct.categories.serializers import EventSerializer
from VolunteerAct.categories.utils import count_events, extract_keywords
from VolunteerAct.favourites.models import Favourites
from VolunteerAct.home.utils import get_emergency_events


def category_details(request, pk):
    category_images_form = CategoryImagesForm(request.POST or None, request.FILES or None)

    category = Category.objects.get(pk=pk)
    category_name_for_url = category.name.replace('&', '%26')
    category.category_name_for_url = category_name_for_url

    upcoming_events = category.category_events.filter(time__gte=timezone.now()).order_by('-time')
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

    all_category_locations = set([event.city for event in category.category_events.all()[:3]])
    all_category_locations = ', '.join(all_category_locations)

    category_images = CategoryImages.objects.filter(category=category)
    user_events_in_this_category = Event.objects.filter(host=request.user, category=category)

    if request.method == "POST":
        if category_images_form.is_valid():
            image = category_images_form.save(commit=False)
            image.author = request.user
            image.category = category

            image.save()
            return redirect('category-page', pk=pk)

    context = {
        'category': category,
        'category_images_form': category_images_form,
        'category_images': category_images,
        'user_events_in_this_category': user_events_in_this_category,
        'upcoming_events': upcoming_events[:2],
        'past_events': past_events[:2],
        'count_upcoming_events': count_events(len(upcoming_events), 2),
        'count_past_events': count_events(len(past_events), 2),
        'active_members': active_members[:36],
        'all_category_locations': all_category_locations,
        'emergency_events': get_emergency_events()
    }

    return render(request, 'categories/category_page.html', context=context)


@login_required
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
        'all_events': all_events,
        'emergency_events': get_emergency_events()
    }

    return render(request, 'categories/all_events_page.html', context=context)


def my_events_view(request):
    upcoming_host_events = request.user.host_events.filter(time__gte=timezone.now()).order_by('-time')
    past_host_events = request.user.host_events.filter(time__lt=timezone.now()).order_by('time')

    members_upcoming_events = [event.attendees.all() for event in upcoming_host_events]
    if members_upcoming_events:
        members_upcoming_events = list(members_upcoming_events[0])  # get the queryset inside a list

    members_past_events = [event.attendees.all() for event in past_host_events]
    if members_past_events:
        members_past_events = list(members_past_events[0])

    active_members = members_upcoming_events + members_past_events

    context = {
        'upcoming_host_events': upcoming_host_events,
        'past_host_events': past_host_events,
        'count_upcoming_events': count_events(len(upcoming_host_events), 2),
        'count_past_events': count_events(len(past_host_events), 2),
        'active_members': active_members[:36],
        'emergency_events': get_emergency_events()
    }

    return render(request, 'categories/my_events_page.html', context=context)


def emergency_events_view(request):
    emergency_events = Event.objects.filter(is_emergency=True)

    context = {
        'emergency_events': emergency_events,
    }

    return render(request, 'categories/emergency_events_page.html', context=context)


def create_event_view(request, categoryId=''):
    form = EventForm(request.POST or None, request.FILES or None)

    context = {}

    if categoryId:
        category = Category.objects.filter(id=categoryId).first()
        form.fields['category'].initial = category

    if request.method == "GET":
        emergency = request.GET.get('emergency')

        if emergency:
            context['emergency'] = emergency

    if request.method == 'POST':
        if form.is_valid():
            event = form.save(commit=False)
            event.host = request.user

            is_emergency = request.GET.get('emergency')
            if is_emergency:
                event.is_emergency = True

            event.save()

            event.attendees.add(request.user)
            return redirect('event-page', categoryId=event.category.id, pk=event.id)

    context['form'] = form
    context['emergency_events'] = get_emergency_events()

    return render(request, 'categories/add_new_event_page.html', context=context)


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

        context['emergency_events'] = get_emergency_events()

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
        if self.get_object().host == self.request.user or self.request.user.is_staff:
            return True

        return False

    def handle_no_permission(self):
        raise PermissionDenied()
    
    def form_invalid(self, form):
        print(form.fields['category'].initial)
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['emergency_events'] = get_emergency_events()

        return context

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


class AttendEventSendEmailAPIView(APIView):

    def post(self, request, event_id):
        event = Event.objects.filter(id=event_id).first()

        email_context = {
            'user_first_name': request.user.profile.first_name,
            'event_title': event.title,
            'event_time': event.time,
            'category_name': event.category.name,
            'event_exact_location': event.exact_location(),
            'host_email': event.host.email
        }

        subject = f"You're All Set for {event.title}!"
        to_email = request.user.email
        recipient_list = [to_email]
        template_name = 'emails/attend_event.html'
        convert_to_html_content = render_to_string(
            template_name=template_name,
            context=email_context
        )
        plain_message = strip_tags(convert_to_html_content)

        send_mail(
            subject=subject,
            message=plain_message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=recipient_list,
            html_message=convert_to_html_content,
            fail_silently=True
        )

        return Response(status=status.HTTP_201_CREATED)
