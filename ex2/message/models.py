from django.db import models
from users.models import User
from chats.models import Chat

# Create your models here.
class Message(models.Model):
    text = models.TextField(max_length=100)
    sending_date = models.DateField()
    chat_pointer = models.ForeignKey(Chat, on_delete=models.CASCADE)
    user_sender = models.ForeignKey(User, on_delete=models.CASCADE)

