from django.contrib.auth import get_user_model
from django.utils import timezone
from rest_framework import serializers

from VolunteerAct.categories.models import Event
from VolunteerAct.favourites.models import Favourites

AppUserModel = get_user_model()


class EventSerializer(serializers.ModelSerializer):
    exact_location = serializers.SerializerMethodField()
    poster_image_full_url = serializers.SerializerMethodField()
    event_time_formatted = serializers.SerializerMethodField()
    already_passed = serializers.SerializerMethodField()
    saved_to_favourites_by_user = serializers.SerializerMethodField()
    attendees = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=AppUserModel.objects.all(),
        allow_empty=True
    )

    class Meta:
        model = Event
        fields = '__all__'

    def get_exact_location(self, obj):
        if obj.city != 'online_event' and obj.location != 'online_event':
            return f"{obj.location}, {obj.city}"

        return 'Online'

    def get_poster_image_full_url(self, obj):
        return obj.poster_image.url

    def get_event_time_formatted(self, obj):
        return obj.time.strftime('%b. %d, %Y, %I:%M %p')

    def get_already_passed(self, obj):
        return True if obj.time < timezone.now() else False

    def get_saved_to_favourites_by_user(self, obj):
        saved_to_favourites_by_logged_in_user = Favourites.objects.all().filter(user=self.context.get('request').user, event=obj).first()

        if saved_to_favourites_by_logged_in_user:
            return True
        else:
            return False
