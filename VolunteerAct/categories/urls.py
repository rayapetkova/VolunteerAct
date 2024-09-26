from django.urls import path

from VolunteerAct.categories.views import CategoryDetailsView, EventDetailsView

urlpatterns = [
    path('<int:pk>/', CategoryDetailsView.as_view(), name='category-page'),
    path('<int:categoryId>/events/<int:pk>', EventDetailsView.as_view(), name='event-page')
]
