from django.db import models

# Create your models here.
class Person(models.Model):
    class Meta:
        abstract = True
    id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=100)

class Employee(Person):
    salary = models.PositiveIntegerField(blank=True, null=True)
    seniority = models.IntegerField(default=0)
    