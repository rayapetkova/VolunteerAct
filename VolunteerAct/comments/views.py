from django.contrib.auth.mixins import UserPassesTestMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from VolunteerAct.comments.models import Comment
from VolunteerAct.comments.serializers import CommentSerializer, CommentCreateSerializer


class CommentListApiView(UserPassesTestMixin, APIView):

    def test_func(self):
        if self.request.user.is_authenticated:
            return True

        return False

    def handle_no_permission(self):
        raise PermissionDenied()

    def get(self, request):
        comments = Comment.objects.all().order_by('-created_at')
        serializer = CommentSerializer(comments, many=True)
        json_data = serializer.data

        return Response(data=json_data)

    def post(self, request):
        serializer = CommentCreateSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentDetailsApiView(UserPassesTestMixin, RetrieveAPIView):
    serializer_class = CommentSerializer

    def test_func(self):
        if self.request.user.is_authenticated:
            return True

        return False

    def handle_no_permission(self):
        raise PermissionDenied()

    def get_queryset(self):
        return Comment.objects.all()


class CommentEditAndDeleteApiView(UserPassesTestMixin, APIView):

    def test_func(self):
        if self.request.user.is_authenticated:
            return True

        return False

    def handle_no_permission(self):
        raise PermissionDenied()

    def patch(self, request, pk):
        comment = Comment.objects.all().filter(id=pk).first()
        serializer = CommentSerializer(comment, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        comment = Comment.objects.all().filter(id=pk).first()
        serializer = CommentSerializer(comment)

        if comment:
            comment.delete()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(status=status.HTTP_400_BAD_REQUEST)
