from django.contrib.auth import login, logout, get_user_model
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView

from VolunteerAct.app_users.forms import AppUserForm, EditAppUserForm
from VolunteerAct.app_users.models import Profile, AppUser

AppUserModel = get_user_model()


class RegisterUserView(CreateView):
    template_name = 'app_users/register_page.html'
    form_class = AppUserForm
    success_url = reverse_lazy('home-page')

    def form_valid(self, form):
        result = super().form_valid(form)

        login(self.request, self.object)

        return result


class LoginUserView(LoginView):
    template_name = 'app_users/login_page.html'
    success_url = reverse_lazy('home-page')


class ProfileUpdateView(UpdateView):
    form_class = EditAppUserForm
    template_name = 'app_users/edit_profile.html'

    def get_object(self, queryset=None):
        user = self.request.user
        profile = Profile.objects.filter(user=user).first()
        return profile

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['form'].fields['email'].initial = self.request.user.email

        return context

    def get_success_url(self):
        return reverse('edit-profile')


def logout_view(request):
    logout(request)
    return redirect('home-page')
