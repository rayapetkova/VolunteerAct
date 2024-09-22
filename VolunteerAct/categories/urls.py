from django.urls import path

from VolunteerAct.categories.views import CategoryDetailsView

urlpatterns = [
    path('<int:pk>/', CategoryDetailsView.as_view(), name='category-page')
]