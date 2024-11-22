from django.urls import path

from VolunteerAct.cities.views import city_details_view

urlpatterns = [
    path('<str:city_name>/', city_details_view, name='city-details')
]
