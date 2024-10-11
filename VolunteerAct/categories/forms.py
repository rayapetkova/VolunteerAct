from django.forms import ModelForm, widgets

from VolunteerAct.categories.models import Event


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
