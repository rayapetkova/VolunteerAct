from asgiref.sync import sync_to_async
from django.contrib.auth import aget_user
from django.contrib.auth.mixins import UserPassesTestMixin
from django.core.exceptions import PermissionDenied
from django.http import Http404, JsonResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from VolunteerAct.categories.models import Event
from VolunteerAct.comments.models import Comment
from VolunteerAct.comments.serializers import CommentSerializer, CommentCreateSerializer


class CommentListApiView(UserPassesTestMixin, APIView):

    def test_func(self):
        if self.request.user.is_authenticated:
            return True

        return False

    def handle_no_permission(self):
        raise PermissionDenied()

    def get(self, request, eventId):
        event = Event.objects.filter(id=eventId).first()
        comments = Comment.objects.filter(event=event).order_by('-created_at')
        serializer = CommentSerializer(comments, many=True)
        json_data = serializer.data

        return Response(data=json_data)

    def post(self, request, eventId):
        serializer = CommentCreateSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


async def comment_details_async_api_view(request, pk):
    try:
        comment = await Comment.objects.aget(id=pk)
    except:
        raise Http404()

    comment_event = await sync_to_async(lambda: comment.event)()

    user = await aget_user(request)
    profile = await sync_to_async(lambda: user.profile)()

    profile_image_full_url = None
    if await sync_to_async(lambda: profile.profile_image)():
        profile_image_full_url = await sync_to_async(lambda: profile.profile_image.url)()

    result_comment = {
        'id': comment.id,
        'profile_image_full_url': profile_image_full_url,
        'body': comment.body,
        'created_at': comment.created_at,
        'updated_at': comment.updated_at,
        'event': comment_event.id,
        'user': {
            'id': user.id,
            'email': user.email,
            'is_staff': user.is_staff,
            'profile': {
                'profile_image': profile.profile_image.url,
                'first_name': profile.first_name,
                'last_name': profile.last_name,
                'phone_number': profile.phone_number,
                'bio': profile.bio,
                'user': user.id
            }
        }
    }

    return JsonResponse(result_comment)


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
