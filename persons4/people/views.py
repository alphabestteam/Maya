from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from people.models import Person
from people.serializers import PersonSerializer
from rest_framework import status
# Create your views here.

@csrf_exempt
def get_people(request):
    if request.method == 'GET':
        persons = Person.objects.all()
        serializer = PersonSerializer(persons, many=True)
        return HttpResponse(serializer.data, status=status.HTTP_201_CREATED)
    
@csrf_exempt
def add_person(request):
    if request.method == 'POST':
        request_data = JSONParser().parse(request)
        serializer = PersonSerializer(data = request_data)
        person = Person(
            name = request_data["name"],
            person_id = request_data["person_id"],
            date_of_birth = request_data["date_of_birth"],
            city = request_data["city"] 
        )
        if serializer.is_valid():
            person.save()
            return HttpResponse(status=status.HTTP_201_CREATED)
        return HttpResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
def update_person(request):
    # Implement here an update function
    if request.method == 'PUT':
        request_data = JSONParser().parse(request)
        pk = request_data.get('person_id', None)
        person = Person.objects.get(person_id=pk)
        serializer = PersonSerializer(person, data=request_data)
        if serializer.is_valid():
            person.name = request_data["name"]
            person.person_id = request_data["person_id"]
            person.date_of_birth = request_data["date_of_birth"]
            person.city = request_data["city"]
            person.save()
            return HttpResponse(serializer.data, status=status.HTTP_201_CREATED)
        return HttpResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@csrf_exempt
def remove_person(request, person_id):
    # Implement here a delete function
    if request.method == 'DELETE':
        try:
            person = Person.objects.get(person_id=person_id)
        except:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)
        person.delete()
        return HttpResponse(status=status.HTTP_201_CREATED)
