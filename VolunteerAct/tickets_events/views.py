from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import UserPassesTestMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import render
from django.utils import timezone
from rest_framework.response import Response
from rest_framework.views import APIView

from VolunteerAct.categories.serializers import EventSerializer
from VolunteerAct.home.utils import get_emergency_events


@login_required
def all_tickets_events_view(request):
    user_tickets_events = request.user.events.all()

    for ticket_event in user_tickets_events:
        ticket_event.already_passed = True if ticket_event.time < timezone.now() else False

    context = {
        'user_tickets_events': user_tickets_events,
        'emergency_events': get_emergency_events()
    }

    return render(request, 'tickets_events/user_tickets_events.html', context=context)


class AllTicketsUserApiView(UserPassesTestMixin, APIView):

    def test_func(self):
        if self.request.user.is_authenticated:
            return True

        return False

    def handle_no_permission(self):
        raise PermissionDenied()

    def get(self, request):
        searched_title = request.GET['searchedTitle']
        events = request.user.events.all().filter(title__icontains=searched_title)
        serializer = EventSerializer(events, many=True)
        json_data = serializer.data

        return Response(data=json_data)
