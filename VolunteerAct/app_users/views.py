from django.contrib.auth import login, logout, get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import Group
from django.contrib.auth.views import LoginView
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
        return not self.request.user.is_authenticated

    def handle_no_permission(self):
        return redirect('home-page')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['emergency_events'] = get_emergency_events()

        return context

    def form_valid(self, form):
        result = super().form_valid(form)

        login(self.request, self.object, backend='django.contrib.auth.backends.ModelBackend')
        group = Group.objects.filter(name='regular_users').first()
        self.object.groups.add(group)

        email_context = {
            'first_name': form.cleaned_data['first_name'],
        }

        subject = 'Welcome to VolunteerAct!'
        to_email = form.cleaned_data['email']
        recipient_list = [to_email]
        template_name = 'emails/welcome_to_volunteeract.html'
        convert_to_html_content = render_to_string(
            template_name=template_name,
            context=email_context
        )
        plain_message = strip_tags(convert_to_html_content)

        send_mail(
            subject=subject,
            message=plain_message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=recipient_list,
            html_message=convert_to_html_content,
            fail_silently=True
        )

        return result


class LoginUserView(UserPassesTestMixin, LoginView):
    template_name = 'app_users/login_page.html'
    success_url = reverse_lazy('home-page')

    def test_func(self):
        return not self.request.user.is_authenticated

    def handle_no_permission(self):
        return redirect('home-page')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['emergency_events'] = get_emergency_events()

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
        'emergency_events': get_emergency_events()
    }

    return render(request, 'app_users/delete_profile.html', context=context)


def logout_view(request):
    logout(request)
    return redirect('home-page')
