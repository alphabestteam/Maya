from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from users.models import User
from chats.models import Chat

# Create your models here.
class Form(models.Model):
    opening_date = models.DateField()
    closing_date = models.DateField()
    user_reporter = models.ForeignKey(User,null=False, on_delete=models.CASCADE)
    status_options = (
        ('Open', 'Open'),
        ('Closed', 'Closed'),
        ('Waiting for Response', 'Waiting for Response'),
        ('Waiting for Handling', 'Waiting for Handling'),
    )
    event_status = models.CharField(max_length=100, choices=status_options)
    can_draft = models.BooleanField(default=False)
    can_download = models.BooleanField(default=False)
    shared_users = models.ManyToManyField(User, related_name='shared_events', blank=True)

class SharedForm(Form):
    uploading_date = models.DateField()
    uploading_user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    file = models.FileField(upload_to='forms/')

class MessagesForm(Form):
    chat_id = models.ForeignKey(Chat, on_delete=models.CASCADE)
    message_history = models.JSONField()