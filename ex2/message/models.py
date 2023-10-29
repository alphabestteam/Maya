from django.db import models
from chats.models import Chat

# Create your models here.
class Message(models.Model):
    text = models.TextField(max_length=100)
    sending_date = models.DateField()
    chat_pointer = models.ForeignKey(Chat, on_delete=models.CASCADE)
    user_sender = models.ForeignKey(to='users.User', on_delete=models.CASCADE)
    message_read = models.BooleanField(default=False)
    receiver = models.ForeignKey(to='users.User', on_delete=models.CASCADE, related_name="receiver_user")


