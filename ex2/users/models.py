from django.db import models
from django.core.validators import MinValueValidator
# Create your models here.
class User(models.Model):
    first_name = models.TextField(max_length=100)
    last_name = models.TextField(max_length=100)
    username = models.TextField(max_length=100, unique=True)
    user_id = models.AutoField(primary_key=True, editable=False)
    email = models.EmailField()
    unread_messages = models.ManyToManyField(to='message.Message', editable=False)