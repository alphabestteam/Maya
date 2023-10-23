from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from users.models import User
from forms.models import Form

# Create your models here.
class Messages(models.Model):
    text = models.TextField(max_length=100)
    sending_date = models.DateField()
    # chat_pointer = models.BooleanField()
    user_sender = models.ForeignKey(User, on_delete=models.CASCADE)

