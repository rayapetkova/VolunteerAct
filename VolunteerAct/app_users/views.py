from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView

from VolunteerAct.app_users.forms import AppUserForm
from VolunteerAct.app_users.models import Profile


class RegisterUserView(CreateView):
    template_name = 'app_users/register_page.html'
    form_class = AppUserForm
    success_url = reverse_lazy('home-page')

    def form_valid(self, form):
        result = super().form_valid(form)

        login(self.request, self.object)


class LoginUserView(LoginView):
    template_name = 'app_users/login_page.html'
    success_url = reverse_lazy('home-page')


class ProfileUpdateView(UpdateView):
    model = Profile
    template_name = 'app_users/edit_profile.html'
    fields = ('first_name', 'last_name', 'phone_number', 'bio')

    def get_success_url(self):
        return reverse('edit-profile', kwargs={
            "pk": self.request.user.profile.id
        })
