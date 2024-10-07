from django.forms import ModelForm, widgets

from VolunteerAct.categories.models import Event


class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ('title', 'details', 'city', 'location', 'time', )

        widgets = {
            'time': widgets.DateTimeInput(
                format=('%Y-%m-%d %H:%M:%S'),
                attrs={'type': 'datetime-local'}
            )
        }
