from django.urls import path

from VolunteerAct.app_users.views import RegisterUserView, LoginUserView

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name="register-user"),
    path('login/', LoginUserView.as_view(), name="login-user")
]