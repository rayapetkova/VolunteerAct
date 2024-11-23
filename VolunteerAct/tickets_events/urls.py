from django.urls import path

from VolunteerAct.tickets_events.views import all_tickets_events_view, AllTicketsUserApiView

urlpatterns = [
    path('', all_tickets_events_view, name='all-user-tickets-events'),
    path('api/', AllTicketsUserApiView.as_view(), name='list-all-user-tickets-api-view')
]
