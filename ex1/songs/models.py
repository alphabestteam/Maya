from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Song(models.Model):
    song_name = models.TextField(max_length=100)
    song_id = models.IntegerField(MinValueValidator(0), primary_key=True)
    released_date = models.DateField()
    singer_name = models.TextField(max_length=100)
