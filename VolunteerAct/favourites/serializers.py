from rest_framework import serializers

from VolunteerAct.favourites.models import Favourites


class FavouritesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Favourites
        fields = '__all__'
