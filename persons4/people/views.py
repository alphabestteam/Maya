from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from people.models import Person, Parent
from people.serializers import PersonSerializer, ParentSerializer, GetParentsSerializer
from rest_framework import status
from rest_framework.renderers import JSONRenderer
from datetime import date
# Create your views here.

@csrf_exempt
def get_people(request):
    """
    a function that gets all people from db
    """
    if request.method == 'GET':
        persons = Person.objects.all()
        serializer = PersonSerializer(persons, many=True)
        return HttpResponse(serializer.data, status=status.HTTP_201_CREATED)
    
@csrf_exempt
def add_person(request):
    """
    a function that adds a new person to db
    """
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
    """
    a function that updates a person 
    """
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
    """
    a function that removes a person from db
    """
    if request.method == 'DELETE':
        try:
            person = Person.objects.get(person_id=person_id)
        except:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)
        person.delete()
        return HttpResponse(status=status.HTTP_201_CREATED)


# EXERCISE 5

@csrf_exempt
def get_parents(request):
    """
    a function that get all parents from db
    """
    if request.method == 'GET':
        parents = Parent.objects.all()
        serializer = ParentSerializer(parents, many=True)
        return HttpResponse(serializer.data, status=status.HTTP_200_OK)
    
@csrf_exempt
def add_parent(request):
    """
    a function that add a parent to db
    """
    if request.method == 'POST':
        request_data = JSONParser().parse(request)
        parent = Parent.objects.create(name = request_data["name"],
            person_id = request_data["person_id"],
            date_of_birth = request_data["date_of_birth"],
            city = request_data["city"],
            work_place = request_data["work_place"],
            basic_salary = request_data["basic_salary"])
        parent.save()
        kids_list = request_data["kids"]
        for kid_id in kids_list:
            kid = Person.objects.get(person_id=kid_id)
            parent.kids.add(kid)
        return HttpResponse(status=status.HTTP_201_CREATED)


@csrf_exempt
def update_parent(request):
    """
    a function that updates a parent 
    """
    if request.method == 'PUT':
        request_data = JSONParser().parse(request)
        pk = request_data.get('person_id', None)
        try:
            parent = Parent.objects.get(person_id=pk)
        except:
            return HttpResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer = ParentSerializer(parent, data=request_data, partial=True)
        if serializer.is_valid():
            serializer.save()
            kid = request_data.get("kids")
            if kid:
                parent.kids.set(kid)
            return HttpResponse(serializer.data, status=status.HTTP_201_CREATED)
        return HttpResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@csrf_exempt
def remove_parent(request, person_id):
    """
    a function that removes a parent from db
    """
    if request.method == 'DELETE':
        try:
            parent = Parent.objects.get(person_id=person_id)
        except:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)
        parent.delete()
        return HttpResponse(status=status.HTTP_200_OK)
    return HttpResponse(status=status.HTTP_404_NOT_FOUND)

@csrf_exempt
def api_connect_kid_parent(request):
    """
    a function that connects kid to his parent
    """
    request_data = JSONParser().parse(request)
    parent_id = request_data.get('parent_id', None)
    kid_id = request_data.get('kid_id', None)
    try:
        parent = Parent.objects.get(person_id=parent_id)
        kid = Person.objects.get(person_id=kid_id)
    except:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    parent.kids.add(kid)
    return HttpResponse(status=status.HTTP_200_OK)

@csrf_exempt
def api_get_parent(request):
    """
    a function that gets a specific parent
    """
    request_data = JSONParser().parse(request)
    parent_id = request_data.get('parent_id', None)
    try:
        parent = Parent.objects.get(person_id=parent_id)
    except:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    parent_serializer = ParentSerializer(parent)
    kids = parent.kids.all()
    kids_serializer = PersonSerializer(kids, many=True) 
    parent_kids_info = {
        "parent": parent_serializer.data,
        "kids": kids_serializer.data,
    }
    return HttpResponse(JSONRenderer().render(parent_kids_info), status=status.HTTP_200_OK)

@csrf_exempt
def find_rich_kids(request):
    """
    a function that finds rich kids and returns a list of them
    """                               
    rich_parents = Parent.objects.filter(basic_salary__gte=50000)
    rich_kids = []
    for parent in rich_parents:
        kids = parent.kids.all()
        for kid in kids:
            age = date.today().year - kid.date_of_birth.year - ((date.today().month, kid.date_of_birth.day) < (date.today().month, kid.date_of_birth.day))
            if age < 18:
                kid_serializer = PersonSerializer(kid) 
                rich_kids.append(kid_serializer.data)
    return HttpResponse(JSONRenderer().render(rich_kids), status=status.HTTP_200_OK)

def get_parents_names(request, person_id):
    """
    a function that returns the names of a person's parents
    """
    parents = Parent.objects.filter(kids=person_id)
    serializer = ParentSerializer(parents, many=True)
    parent_data = serializer.data
    # serializer = GetParentsSerializer(parents, partial=True)
    parent_names = [parent['name'] for parent in parent_data]
    return HttpResponse(JSONRenderer().render(parent_names), status=status.HTTP_200_OK)

def get_kids(request):
    """
    a function that get all kids of a parent
    """
    request_data = JSONParser().parse(request)
    parent_id = request_data.get('parent_id', None)
    parent = Parent.objects.get(person_id=parent_id)
    kids = parent.kids.all()
    serializer = ParentSerializer(kids, many = True)
    return HttpResponse(serializer.data, status = status.HTTP_200_OK)

def get_grandparents(request):
    """
    a function that gets the grandparents of a person
    """
    request_data = JSONParser().parse(request)
    person_id = request_data.get('person_id', None)
    try:
        person = Person.objects.get(person_id=person_id)
    except:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    parents = Parent.objects.filter(kids=person_id)
    grandparents_names = []
    for parent in parents:
        grandparents = Parent.objects.filter(kids=parent.person_id)
        grandparents_names.extend([grand.name for grand in grandparents])
    return HttpResponse(JSONRenderer().render(grandparents_names), status = status.HTTP_200_OK)

def find_siblings(request):
    """
    a function that finds the siblings of a person
    """
    request_data = JSONParser().parse(request)
    person_id = request_data.get('person_id', None)
    try:
        person = Person.objects.get(person_id=person_id)
    except:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    parents = list(Parent.objects.filter(kids=person_id))
    siblings = []
    for parent in parents:
        kids = parent.kids.all()
        for kid in kids:
            if kid.person_id != person_id:
                siblings.append(kid.name)
    return HttpResponse(siblings, status = status.HTTP_200_OK)