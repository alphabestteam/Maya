from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class User(models.Model):
    first_name = models.TextField(max_length=100)
    last_name = models.TextField(max_length=100)
    username = models.TextField(max_length=100)
    user_id = models.IntegerField(MinValueValidator(0), primary_key=True)
    email = models.EmailField()
    unread_messages = models.IntegerChoices(MinValueValidator(0))