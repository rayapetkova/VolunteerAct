from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from VolunteerAct.favourites.serializers import FavouritesSerializer


class FavouritesCreateApiView(APIView):

    def post(self, request):
        serializer = FavouritesSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)