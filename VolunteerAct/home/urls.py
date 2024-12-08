from django.urls import path

from VolunteerAct.home.views import home_page, contact_us_page, about_us_page

urlpatterns = [
    path('', home_page, name='home-page'),
    path('contact_us/', contact_us_page, name='contact-us'),
    path('about_us/', about_us_page, name='about-us')
]
