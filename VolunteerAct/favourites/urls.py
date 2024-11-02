from django.urls import path

from VolunteerAct.favourites.views import FavouritesCreateApiView

urlpatterns = [
    path('', FavouritesCreateApiView.as_view(), name='list-create-favourites-record')
]
