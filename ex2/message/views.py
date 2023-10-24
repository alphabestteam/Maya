from rest_framework import viewsets
from .models import Message
from .serializers import MessageSerializer
from chats.models import Chat
from chats.serializers import ChatSerializer
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404


# Create your views here.

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def create(self, request):
        serializer = MessageSerializer(data=request.data)
        chat = request.data.get("chat_pointer")
        exist = Chat.objects.filter(chat_id=chat).exists()
        if not exist:
            serializer = ChatSerializer(data={"chat_id": chat})
            if serializer.is_valid():
                serializer.save()
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)


