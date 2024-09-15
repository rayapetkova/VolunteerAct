from django.shortcuts import render
from django.views.generic import CreateView

from VolunteerAct.app_users.forms import AppUserForm


class RegisterUserView(CreateView):
    template_name = 'app_users/register_page.html'
    form_class = AppUserForm
