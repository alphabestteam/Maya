from django.db import models
from django.core.validators import MinValueValidator


# Create your models here.
class Chat(models.Model):
    chat_id = models.IntegerField(MinValueValidator(0), primary_key=True)

