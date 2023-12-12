from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from .models import Location
# Create your views here.
@csrf_exempt
def get_people(request):
    """
    a function that gets all people from db
    """
    if request.method == 'GET':
        persons = Location.objects.all()
        serializer = LocationSerializer(persons, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)