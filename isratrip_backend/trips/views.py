from django.shortcuts import render
from rest_framework import viewsets
from .models import Trip, RequestedTrip
from .serializers import TripSerializer, RequestedTripSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from locations.models import Location
from locations.serializers import LocationSerializer
from categories.models import Category
from categories.serializers import CategorySerializer

# Create your views here.
class ListTrips(APIView):
    def get(self, request):
        """
        a function that gets all trips from db
        """
        locations = Trip.objects.all()
        serializer = TripSerializer(locations, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class RequestedTripViewSet(viewsets.ModelViewSet):
    queryset = RequestedTrip.objects.all()
    serializer_class = RequestedTripSerializer

    def create(self, request):
        location_name = request.data.get("location")
        categories = request.data.get("categories")
        category_ids = []
        location_id = 0
        location_exists = Location.objects.filter(location_name=location_name).exists()
        for index in range(len(categories)):
            categories_exist = Category.objects.filter(category_name=categories[index]).exists()
            if not categories_exist:
                category_serializer = CategorySerializer(data={"category_name": categories[index]})
                if category_serializer.is_valid():
                    category_serializer.save()
            category = Category.objects.get(category_name=categories[index])
            category_ids.append(category.category_id)
        if not location_exists:
            location_serializer = LocationSerializer(data={"location_name": location_name})
            if location_serializer.is_valid():
                location_serializer.save()
        else:
            location = Location.objects.get(location_name=location_name)
            location_id = location.location_id
        req_trip_serializer = RequestedTripSerializer(data={"location": location_id, 
                                                            "categories": category_ids,
                                                            "trip_title": request.data.get('trip_title'),
                                                            "trip_description": request.data.get('trip_description'),
                                                            "user_id": request.data.get('user_id'),
                                                            "age_limit": request.data.get('age_limit'),
                                                            "best_weather": request.data.get('best_weather'),
                                                            "is_open": request.data.get('is_open'),
                                                            })
        if req_trip_serializer.is_valid():
            req_trip_serializer.save()
            return Response(req_trip_serializer.data, status=status.HTTP_201_CREATED)
        return Response({"detail": "Validation failed"}, status=status.HTTP_406_NOT_ACCEPTABLE)

    def put():
        return Response({"detail": "Method 'PUT' not allowed."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)