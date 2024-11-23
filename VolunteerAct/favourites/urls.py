from django.urls import path

from VolunteerAct.favourites.views import FavouritesCreateApiView, favourite_events_view, FavouritesDeleteApiView, \
    FavouritesDeleteByEventAndUserIdsApiView, AllFavouriteEventsApiView

urlpatterns = [
    path('', favourite_events_view, name='user-favourite-events-page'),
    path('api/', FavouritesCreateApiView.as_view(), name='list-create-favourites-record-api'),
    path('api/all/', AllFavouriteEventsApiView.as_view(), name='list-all-favourite-events-api'),
    path('api/<int:pk>/', FavouritesDeleteApiView.as_view(), name='delete-favourite-record-api'),
    path('api/<int:event_id>/delete/', FavouritesDeleteByEventAndUserIdsApiView.as_view(), name='delete-favourite-record-by-event-and-user-api')
]
