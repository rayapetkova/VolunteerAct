from django.contrib.auth import get_user_model
from rest_framework import serializers

from VolunteerAct.app_users.models import Profile

AppUserModel = get_user_model()


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = '__all__'


class AppUserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(many=False)

    class Meta:
        model = AppUserModel
        fields = '__all__'
