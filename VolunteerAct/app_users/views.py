from decouple import config
from django.contrib.auth import login, logout, get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import Group
from django.contrib.auth.views import LoginView
from django.core.exceptions import PermissionDenied
from django.core.mail import send_mail
from django.http import Http404
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.utils.html import strip_tags
from django.views.generic import CreateView, UpdateView, DetailView
from django.conf import settings

from VolunteerAct.app_users.forms import AppUserForm, EditAppUserForm, DeleteAppUserForm
from VolunteerAct.app_users.models import Profile
from VolunteerAct.home.utils import get_emergency_events

AppUserModel = get_user_model()


class RegisterUserView(UserPassesTestMixin, CreateView):
    template_name = 'app_users/register_page.html'
    form_class = AppUserForm
    success_url = reverse_lazy('home-page')

    def test_func(self):
        if self.request.user.is_authenticated:
            return False

        return True

    def handle_no_permission(self):
        return redirect('home-page')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['emergency_events'] = get_emergency_events()
        context['video_url'] = config('VIDEO_URL')

        return context

    def form_valid(self, form):
        result = super().form_valid(form)

        login(self.request, self.object, backend='django.contrib.auth.backends.ModelBackend')

        return result


class LoginUserView(UserPassesTestMixin, LoginView):
    template_name = 'app_users/login_page.html'
    success_url = reverse_lazy('home-page')

    def test_func(self):
        if self.request.user.is_authenticated:
            return False

        return True

    def handle_no_permission(self):
        return redirect('home-page')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['emergency_events'] = get_emergency_events()
        context['video_url'] = config('VIDEO_URL')

        return context


class ProfileView(LoginRequiredMixin, UpdateView, DetailView):
    model = Profile
    form_class = EditAppUserForm

    def get_template_names(self):
        user = self.request.user

        if user.profile.id == self.kwargs['pk']:
            return ['app_users/edit_profile.html']

        return ['app_users/profile_page.html']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['form'].fields['email'].initial = self.request.user.email
        context['emergency_events'] = get_emergency_events()
        context['video_url'] = config('VIDEO_URL')

        return context

    def get_success_url(self):
        return reverse_lazy('profile-details-update', kwargs={
            'pk': self.object.id
        })


def delete_profile_view(request):
    if not request.user.is_authenticated:
        raise Http404()

    user_profile = request.user.profile
    form = DeleteAppUserForm(instance=user_profile)
    form.fields['email'].initial = user_profile.user.email

    if request.method == "POST":
        request.user.delete()
        return redirect('home-page')

    context = {
        'form': form,
        'emergency_events': get_emergency_events(),
        'video_url': config('VIDEO_URL')
    }

    return render(request, 'app_users/delete_profile.html', context=context)


def logout_view(request):
    if request.user.is_authenticated:
        logout(request)

    return redirect('home-page')
