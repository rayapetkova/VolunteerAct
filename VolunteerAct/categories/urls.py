from django.urls import path

from VolunteerAct.categories.views import category_details, EventDetailsView, all_events_view, EventUpdateView, \
    EventListAPIView, EventUpdateAPIView, AttendEventSendEmailAPIView, my_events_view, create_event_view, \
    emergency_events_view, event_comments_view

urlpatterns = [
    path('<int:pk>/', category_details, name='category-page'),
    path('<int:categoryId>/events/<int:pk>/', EventDetailsView.as_view(), name='event-page'),
    path('<int:categoryId>/events/<int:pk>/comments/', event_comments_view, name='event-comments-page'),
    path('events/add/', create_event_view, name='create-new-event-page'),
    path('<int:categoryId>/events/add/', create_event_view, name='create-new-event-page-with-category'),
    path('<int:categoryId>/events/<int:pk>/edit/', EventUpdateView.as_view(), name='edit-event'),
    path('events/', all_events_view, name='all-events-page'),
    path('my_events/', my_events_view, name='my-events-page'),
    path('emergency_events/', emergency_events_view, name='emergency-events-page'),
    path('events/api/', EventListAPIView.as_view(), name='list-events-api'),
    path('events/api/update/<int:pk>', EventUpdateAPIView.as_view(), name='update-event-api'),
    path('events/api/send_email/<int:event_id>/', AttendEventSendEmailAPIView.as_view(), name='send-email-attend-event-api')
]
