from django.shortcuts import render
from .serializers import CategorySerializer
from rest_framework import status
from rest_framework.views import APIView
from .models import Category
from rest_framework.response import Response

# Create your views here.
class ListCategories(APIView):
    def get(self, request):
        """
        a function that gets all categories from db
        """
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    def create(self, request):
        """
        a function that add a category to db
        """
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)    