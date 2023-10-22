from django.test import TestCase
from people.models import Person
from . import views
from people.serializers import PersonSerializer, ParentSerializer, GetParentsSerializer
from rest_framework import status
from django.http import HttpResponse, JsonResponse, HttpRequest
from django.test import Client
import json


# Create your tests here.
class PersonTestCase(TestCase):
    def setUp(self) -> None:
        # Q1: 
        Person.objects.create(name = "test right", person_id = 22, date_of_birth = '2004-09-05', city = "Shoham")
        Person.objects.create(name = "test wrong", person_id = 23, date_of_birth = '2011-09-05', city = "Shoham")

    def test_age(self):
        """
        Q1: a test that checks if the function is_above_eighteen() is working
        """
        test_right = Person.objects.get(name="test right")
        test_wrong = Person.objects.get(name="test wrong")
        self.assertTrue(test_right.is_above_eighteen())
        self.assertFalse(test_wrong.is_above_eighteen())
    
    def test_get_people(self):
        """
        A test that checks if the function get_all_people() works
        """
        client = Client()
        request = HttpRequest()
        request.method = 'GET'
        response = client.get('/api/getAllPeople/')
        self.assertEqual(response.status_code, 200)
        persons = Person.objects.all()
        serializer = PersonSerializer(persons, many=True).data
        self.assertEqual(json.load(response.content.decode('utf-8')), serializer)

