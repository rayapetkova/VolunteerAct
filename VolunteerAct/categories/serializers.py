from django.contrib.auth import get_user_model
from django.utils import timezone
from rest_framework import serializers

from VolunteerAct.categories.models import Event


AppUserModel = get_user_model()


class EventSerializer(serializers.ModelSerializer):
    exact_location = serializers.SerializerMethodField()
    poster_image_full_url = serializers.SerializerMethodField()
    event_time_formatted = serializers.SerializerMethodField()
    already_passed = serializers.SerializerMethodField()
    attendees = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=AppUserModel.objects.all(),
        allow_empty=True
    )

    class Meta:
        model = Event
        fields = '__all__'

    def get_exact_location(self, obj):
        return f"{obj.location}, {obj.city}"

    def get_poster_image_full_url(self, obj):
        return obj.poster_image.url

    def get_event_time_formatted(self, obj):
        return obj.time.strftime('%b. %d, %Y, %I:%M %p')

    def get_already_passed(self, obj):
        return True if obj.time < timezone.now() else False
