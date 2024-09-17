from django.urls import path

from VolunteerAct.home.views import home_page

urlpatterns = [
    path('', home_page)
]