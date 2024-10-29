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

    class Meta:
        model = UserModel
        fields = ('email', 'first_name', 'last_name', 'password1', 'password2')
        labels = {
            "password2": "Confirm password"
        }

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


class EditAppUserForm(forms.ModelForm):
    email = forms.EmailField(required=False)

    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'phone_number', 'email', 'bio', 'profile_image')

        widgets = {
            'bio': forms.Textarea(attrs={
                'rows': 10
            })
        }

        labels = {
            'profile_image': 'Change image'
        }

    def save(self, commit=True):
        profile = super().save(commit=commit)

        user = profile.user
        email = self.cleaned_data['email']
        user.email = email

        if commit:
            user.save()

        return profile


class DeleteAppUserForm(forms.ModelForm):

    email = forms.EmailField()

    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'phone_number', 'email', 'bio')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs['readonly'] = 'readonly'
            self.fields[field].disabled = 'disabled'
        