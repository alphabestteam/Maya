from rest_framework.response import Response
from .models import Location
from .serializers import LocationSerializer
from rest_framework import status
from rest_framework.views import APIView

# Create your views here.
class ListLocations(APIView):
    def get(self, request):
        """
        a function that gets all locations from db
        """
        locations = Location.objects.all()
        serializer = LocationSerializer(locations, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    def create(self, request):
        """
        a function that add a location to db
        """
        serializer = LocationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)