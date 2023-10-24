from rest_framework import serializers
from .models import Form, SharedForm, MessagesForm

class FormSerializer(serializers.ModelSerializer):
    class Meta:
        model = Form
        fields = '__all__'


class SharedFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = SharedForm
        fields = '__all__'


class MessagesFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessagesForm
        fields = '__all__'
