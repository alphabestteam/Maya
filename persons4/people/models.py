from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=100)
    person_id = models.IntegerField(MinValueValidator(0), primary_key=True)
    date_of_birth = models.DateField(null=True, blank=True)
    city = models.TextField(max_length=100)