from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from VolunteerAct.comments.models import Comment
from VolunteerAct.comments.serializers import CommentSerializer, CommentCreateSerializer


class CommentListApiView(APIView):

    def get(self, request):
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)
        json_data = serializer.data

        return Response(data=json_data)

    def post(self, request):
        serializer = CommentCreateSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentDetailsApiView(RetrieveAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comment.objects.all()
