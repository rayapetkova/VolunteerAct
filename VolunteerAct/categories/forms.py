from django import forms
from django.forms import ModelForm, widgets, Form

from VolunteerAct.categories.models import Event
from VolunteerAct.categories.utils import get_categories, get_cities


class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ('poster_image', 'title', 'details', 'city', 'location', 'time', )

        widgets = {
            'details': widgets.Textarea(
                attrs={'rows': 10}
            ),
            'location': widgets.TextInput(
                attrs={'placeholder': 'E.g. ul. Rakovski'}
            ),
            'time': widgets.DateTimeInput(
                format=('%Y-%m-%d %H:%M:%S'),
                attrs={'type': 'datetime-local'}
            )
        }


class EventEditForm(EventForm):
    pass


class EventDeleteForm(EventForm):
    pass


class FilterForm(Form):
    CATEGORY_CHOICES = get_categories()
    CITY_CHOICES = get_cities()

    TIME_CHOICES = (
        ('Upcoming', 'Upcoming'),
        ('Past', 'Past')
    )

    category = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        required=False,
        choices=CATEGORY_CHOICES
    )

    city = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        required=False,
        choices=CITY_CHOICES
    )

    time = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        required=False,
        choices=TIME_CHOICES
    )
