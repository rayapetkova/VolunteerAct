from rest_framework import serializers

from VolunteerAct.categories.serializers import EventSerializer
from VolunteerAct.favourites.models import Favourites


class FavouritesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Favourites
        fields = '__all__'


class FavouritesSerializerWithEventInfo(serializers.ModelSerializer):
    event = EventSerializer(many=False)

    class Meta:
        model = Favourites
        fields = '__all__'
