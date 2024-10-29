from django.urls import path

from VolunteerAct.app_users.views import RegisterUserView, LoginUserView, ProfileView, logout_view, delete_profile_view

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name="register-user"),
    path('login/', LoginUserView.as_view(), name="login-user"),
    path('logout/', logout_view, name="logout-user"),
    path('delete_profile/', delete_profile_view, name='delete-profile'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile-details-update')
]
