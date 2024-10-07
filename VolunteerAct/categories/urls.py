from django.urls import path

from VolunteerAct.categories.views import category_details, EventDetailsView

urlpatterns = [
    path('<int:pk>/', category_details, name='category-page'),
    path('<int:categoryId>/events/<int:pk>', EventDetailsView.as_view(), name='event-page')
]
