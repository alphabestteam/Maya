from rest_framework import viewsets
from .models import Message
from .serializers import MessageSerializer
from chats.models import Chat
from chats.serializers import ChatSerializer
from rest_framework.response import Response
from rest_framework import status
from users.models import User
from users.serializers import UserSerializer

# Create your views here.

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def create(self, request):
        message_serializer = MessageSerializer(data=request.data)
        chat = request.data.get("chat_pointer")
        exist = Chat.objects.filter(chat_id=chat).exists()
        if not exist:
            chat_serializer = ChatSerializer(data={"chat_id": chat})
            if chat_serializer.is_valid():
                chat_serializer.save()
        if message_serializer.is_valid():
            message_serializer.save()
            user_id = request.data.get('user_sender', None)
            message_read = request.data.get('message_read', False)
            if not message_read:
                user = User.objects.get(user_id=user_id)
                user.unread_messages.add(message_serializer.instance)
            return Response(message_serializer.data, status=status.HTTP_201_CREATED)

