from PIL import Image
from cloudinary import CloudinaryResource
from django import forms
from django.core.exceptions import ValidationError
from django.forms import ModelForm, widgets, Form
from django.utils import timezone

from VolunteerAct.categories.models import Event, CategoryImages
from VolunteerAct.categories.utils import get_categories, get_cities


class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ('category', 'poster_image', 'title', 'details', 'online', 'city', 'location', 'online_meeting_link', 'time', )

        widgets = {
            'details': widgets.Textarea(
                attrs={'rows': 10}
            ),
            'city': widgets.TextInput(
                attrs={'placeholder': 'E.g. Sofia'}
            ),
            'location': widgets.TextInput(
                attrs={'placeholder': 'E.g. ul. Rakovski'}
            ),
            'time': widgets.DateTimeInput(
                format=('%Y-%m-%d %H:%M:%S'),
                attrs={'type': 'datetime-local'}
            ),
            'online_meeting_link': widgets.URLInput(
                attrs={'placeholder': 'https://'}
            )
        }

    def clean_poster_image(self):
        poster_image = self.cleaned_data['poster_image']

        if isinstance(poster_image, CloudinaryResource):
            return poster_image

        try:
            img = Image.open(poster_image)
            img.verify()

            return poster_image
        except:
            raise ValidationError('Poster picture needs to be an image.')

    def clean_time(self):
        time = self.cleaned_data['time']

        if time < timezone.now():
            raise ValidationError("The event's time needs to be in the future.")

        return time


class CategoryImagesForm(ModelForm):

    class Meta:
        model = CategoryImages
        fields = ('image', )

    def clean_image(self):
        image = self.cleaned_data['image']

        if isinstance(image, CloudinaryResource):
            return image

        try:
            img = Image.open(image)
            img.verify()

            return image
        except:
            raise ValidationError('Picture needs to be an image.')


class EventEditForm(EventForm):
    pass


class EventDeleteForm(EventForm):
    pass


class FilterForm(Form):
    CATEGORY_CHOICES = []
    CITY_CHOICES = []

    TIME_CHOICES = (
        ('Upcoming', 'Upcoming'),
        ('Past', 'Past')
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].choices = get_categories()
        self.fields['city'].choices = get_cities()

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
