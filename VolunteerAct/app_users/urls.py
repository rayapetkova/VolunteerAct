from django.urls import path

from VolunteerAct.app_users.views import RegisterUserView, LoginUserView, ProfileUpdateView

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name="register-user"),
    path('login/', LoginUserView.as_view(), name="login-user"),
    path('<int:pk>/edit_profile', ProfileUpdateView.as_view(), name="edit-profile")
]