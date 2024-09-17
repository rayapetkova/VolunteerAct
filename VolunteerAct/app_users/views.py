from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.views.generic import CreateView

from VolunteerAct.app_users.forms import AppUserForm


class RegisterUserView(CreateView):
    template_name = 'app_users/register_page.html'
    form_class = AppUserForm

    def form_valid(self, form):
        result = super().form_valid(form)

        login(self.request, self.object)


class LoginUserView(LoginView):
    template_name = 'app_users/login_page.html'