from django.urls import path

from VolunteerAct.categories.views import category_page

urlpatterns = [
    path('<int:pk>/', category_page, name='category-page')
]