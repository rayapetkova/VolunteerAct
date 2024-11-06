from rest_framework import serializers

from VolunteerAct.categories.models import Event


class EventSerializer(serializers.ModelSerializer):
    exact_location = serializers.SerializerMethodField()
    poster_image_full_url = serializers.SerializerMethodField()
    event_time_formatted = serializers.SerializerMethodField()

    class Meta:
        model = Event
        fields = '__all__'

    def get_exact_location(self, obj):
        return f"{obj.location}, {obj.city}"

    def get_poster_image_full_url(self, obj):
        return obj.poster_image.url

    def get_event_time_formatted(self, obj):
        return obj.time.strftime('%b. %d, %Y, %I:%M %p')
