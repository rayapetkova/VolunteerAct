from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from VolunteerAct.comments.models import Comment
from VolunteerAct.comments.serializers import CommentSerializer


class CommentListApiView(APIView):

    def get(self, request):
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)
        json_data = serializer.data

        return Response(data=json_data)
