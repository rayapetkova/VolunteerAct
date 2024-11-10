from django.urls import path

from VolunteerAct.categories.views import category_details, EventDetailsView, all_events_view, EventUpdateView, \
    EventListAPIView, EventUpdateAPIView

urlpatterns = [
    path('<int:pk>/', category_details, name='category-page'),
    path('<int:categoryId>/events/<int:pk>', EventDetailsView.as_view(), name='event-page'),
    path('<int:categoryId>/events/<int:pk>/edit/', EventUpdateView.as_view(), name='edit-event'),
    path('events/', all_events_view, name='all-events-page'),
    path('events/api/', EventListAPIView.as_view(), name='list-events-api'),
    path('events/api/update/<int:pk>', EventUpdateAPIView.as_view(), name='update-event-api')
]
