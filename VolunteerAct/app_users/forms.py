from django import forms
from django.contrib.auth import forms as auth_forms, get_user_model
from django.utils.translation import gettext_lazy as _

from VolunteerAct.app_users.models import Profile

UserModel = get_user_model()


class AppUserForm(auth_forms.UserCreationForm):
    first_name = forms.CharField(
        max_length=150,
        min_length=2
    )

    last_name = forms.CharField(
        max_length=150,
        min_length=2
    )

    bio = forms.CharField(
        max_length=800,
        min_length=10
    )

    password2 = forms.CharField(
        label=_("Password confirmation"),
        required=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        strip=False,
        help_text=_("Enter the same password as before, for verification."),
    )

    class Meta:
        model = UserModel
        fields = '__all__'

    def save(self, commit=True):
        user = super().save(commit=commit)

        first_name = self.cleaned_data['first_name']
        last_name = self.cleaned_data['last_name']

        profile = Profile(
            first_name=first_name,
            last_name=last_name,
            user=user
        )

        if commit:
            profile.save()

        return user