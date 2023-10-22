from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=100)
    person_id = models.IntegerField(MinValueValidator(0), primary_key=True)
    date_of_birth = models.DateField()
    city = models.TextField(max_length=100)

class Parent(Person):
    work_place = models.CharField(max_length=50, default="")
    basic_salary = models.IntegerField(validators=[MaxValueValidator(999999)], default=0)
    kids = models.ManyToManyField(Person, blank=True, related_name='parents')

