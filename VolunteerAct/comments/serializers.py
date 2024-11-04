from cloudinary.utils import cloudinary_url
from rest_framework import serializers

from VolunteerAct.app_users.serializers import AppUserSerializer
from VolunteerAct.comments.models import Comment


class CommentSerializer(serializers.ModelSerializer):
    user = AppUserSerializer(many=False)
    profile_image_full_url = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ('profile_image_full_url', 'body', 'created_at', 'updated_at', 'event', 'user')

    def get_profile_image_full_url(self, obj):
        if obj.user.profile.profile_image:
            return obj.user.profile.profile_image.url

        return None


class CommentCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'
