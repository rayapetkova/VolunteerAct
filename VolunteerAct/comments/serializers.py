from rest_framework import serializers

from VolunteerAct.app_users.serializers import AppUserSerializer
from VolunteerAct.comments.models import Comment


class CommentSerializer(serializers.ModelSerializer):
    user = AppUserSerializer(many=False)

    class Meta:
        model = Comment
        fields = '__all__'
