from django.urls import path

from VolunteerAct.app_users.views import RegisterUserView

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name="register-user")
]