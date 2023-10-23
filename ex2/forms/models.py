from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from users.models import User

# Create your models here.
class Form(models.Model):
    opening_date = models.DateField()
    closing_date = models.DateField()
    user_reporter = models.ForeignKey(User, on_delete=models.CASCADE)
    status_options = (
        ('Open', 'Open'),
        ('Closed', 'Closed'),
        ('Waiting for Response', 'Waiting for Response'),
        ('Waiting for Handling', 'Waiting for Handling'),
    )
    can_draft = models.BooleanField()
    can_download = models.BooleanField()
    shared_users = models.ManyToManyField(User, related_name='shared_events', blank=True)
