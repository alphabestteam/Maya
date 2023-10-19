from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=100)
    person_id = models.IntegerField(MinValueValidator(0), primary_key=True)
    birthDate = models.DateField()
    homeTown = models.TextField(max_length=100)

class Parent(Person):
    work = models.CharField(max_length=50, default="")
    baseSalary = models.IntegerField(default=0)
    children = models.ManyToManyField(Person, blank=True, related_name='parents')

