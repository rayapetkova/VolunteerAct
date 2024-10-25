from django import forms
from django.db.models import Count
from django.forms import ModelForm, widgets, Form
from django.utils import timezone

from VolunteerAct.categories.models import Event, Category


def get_categories():
    categories = Category.objects.all()
    categories_names_tuple = [(category.name, category.name) for category in categories]

    return categories_names_tuple


def get_cities():
    cities = Event.objects.values('city').annotate(cities_count=Count('city')).order_by('-cities_count')
    cities_tuple = [(cityDict['city'], f"{cityDict['city']} ({cityDict['cities_count']})") for cityDict in cities]

    return cities_tuple


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
