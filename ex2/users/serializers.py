from rest_framework import serializers
from .models import User
from datetime import date

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.username = validated_data.get('username', instance.username)
        instance.user_id = validated_data.get('user_id', instance.user_id)
        instance.email = validated_data.get('email', instance.email)
        instance.unread_messages = validated_data.get('unread_messages', instance.unread_messages)
        instance.save()
        return instance


