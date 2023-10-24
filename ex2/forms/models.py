from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from users.models import User
from chats.models import Chat

# Create your models here.
STATUS_OPTIONS = (
        ('open', 'open'),
        ('closed', 'closed'),
        ('waiting for response', 'Waiting for response'),
        ('waiting for handling', 'Waiting for handling'),
    )
class Form(models.Model):
    opening_date = models.DateField()
    closing_date = models.DateField()
    user_reporter = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    event_status = models.CharField(max_length=100, choices=STATUS_OPTIONS)
    can_draft = models.BooleanField(default=False)
    can_download = models.BooleanField(default=False)
    shared_users = models.ManyToManyField(User, related_name='shared_users', blank=True)

class SharedForm(Form):
    uploading_date = models.DateField()
    uploading_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    file = models.FileField(upload_to='forms/')

class MessagesForm(Form):
    chat_id = models.ForeignKey(Chat, on_delete=models.SET_NULL, null=True)
    message_history = models.JSONField()