from django.db import models

# Create your models here.
class Location(models.Model):
    location_id = models.AutoField(primary_key=True, editable=False)
    location_name = models.TextField(max_length=100, unique=True)