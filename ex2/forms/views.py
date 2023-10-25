from rest_framework import viewsets
from forms.models import Form, SharedForm, MessagesForm
from forms.serializers import FormSerializer, SharedFormSerializer, MessagesFormSerializer
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render, redirect

# Create your views here.

class FormViewSet(viewsets.ModelViewSet):
    queryset = Form.objects.all()
    serializer_class = FormSerializer

class SharedViewSet(viewsets.ModelViewSet):
    queryset = SharedForm.objects.all()
    serializer_class = SharedFormSerializer

class MessagesViewSet(viewsets.ModelViewSet):
    queryset = MessagesForm.objects.all()
    serializer_class = MessagesFormSerializer