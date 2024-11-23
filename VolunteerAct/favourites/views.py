from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils import timezone
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from VolunteerAct.categories.forms import FilterForm
from VolunteerAct.categories.serializers import EventSerializer
from VolunteerAct.favourites.models import Favourites
from VolunteerAct.favourites.serializers import FavouritesSerializer, FavouritesSerializerWithEventInfo


@login_required
def favourite_events_view(request):
    filter_form = FilterForm(request.GET or None)

    user_favourite_events = Favourites.objects.all().filter(user=request.user).order_by('-added_on')

    for favourite_event in user_favourite_events:
        favourite_event.already_passed = True if favourite_event.event.time < timezone.now() else False

    if request.method == "GET":
        if filter_form.is_valid():
            categories_filter = request.GET.getlist('category')
            cities_filter = request.GET.getlist('city')
            time_filter = request.GET.getlist('time')

            if categories_filter:
                user_favourite_events = user_favourite_events.filter(event__category__name__in=categories_filter)

            if cities_filter:
                user_favourite_events = user_favourite_events.filter(event__city__in=cities_filter)

            if len(time_filter) == 1:
                if 'Past' in time_filter:
                    user_favourite_events = user_favourite_events.filter(event__time__lt=timezone.now())

                if 'Upcoming' in time_filter:
                    user_favourite_events = user_favourite_events.filter(event__time__gte=timezone.now())

    context = {
        'filter_form': filter_form,
        'user_favourite_events': user_favourite_events
    }

    return render(request, 'favourites/favourite_events.html', context=context)


class AllFavouriteEventsApiView(APIView):

    def get(self, request):
        searched_title = request.GET['searchedTitle']
        user_favourites = Favourites.objects.all().filter(user=request.user, event__title__icontains=searched_title).order_by('-added_on')

        for favourite_record in user_favourites:
            favourite_record.already_passed = True if favourite_record.event.time < timezone.now() else False

        serializer = FavouritesSerializerWithEventInfo(user_favourites, many=True)
        json_data = serializer.data

        return Response(data=json_data)


class FavouritesCreateApiView(APIView):

    def post(self, request):
        serializer = FavouritesSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


class FavouritesDeleteByEventAndUserIdsApiView(APIView):

    def delete(self, request, event_id):
        favourite_event = Favourites.objects.all().filter(event__id=event_id, user=request.user).first()
        serializer = FavouritesSerializer(favourite_event)

        if favourite_event:
            favourite_event.delete()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(status=status.HTTP_400_BAD_REQUEST)


class FavouritesDeleteApiView(APIView):

    def delete(self, request, pk):
        favourite_event = Favourites.objects.all().filter(id=pk).first()
        serializer = FavouritesSerializer(favourite_event)

        if favourite_event:
            favourite_event.delete()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(status=status.HTTP_400_BAD_REQUEST)
