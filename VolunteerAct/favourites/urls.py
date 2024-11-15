from django.urls import path

from VolunteerAct.favourites.views import FavouritesCreateApiView, favourite_events_view

urlpatterns = [
    path('', favourite_events_view, name='user-favourite-events-page'),
    path('api/', FavouritesCreateApiView.as_view(), name='list-create-favourites-record-api')
]
