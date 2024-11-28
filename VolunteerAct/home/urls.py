from django.urls import path

from VolunteerAct.home.views import home_page, contact_us_page

urlpatterns = [
    path('', home_page, name='home-page'),
    path('contact_us/', contact_us_page, name='contact-us')
]
