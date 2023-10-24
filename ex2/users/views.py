from django.shortcuts import render
from rest_framework.views import APIView
from users.models import User
from users.serializers import UserSerializer
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

# Create your views here.
class ListUsers(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request):
        user_id = request.data.get('user_id', None)
        user = get_object_or_404(User, user_id=user_id)
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        
    def delete(self, request, user_id):
        user = get_object_or_404(User, user_id=user_id)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 
    