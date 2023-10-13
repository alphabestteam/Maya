from rest_framework import serializers
from .models import Target

class TargetSerializer(serializers.ModelSerializer):
    class Meta:
        # define here your model and the fields to serialize
        model = Target
        fields = ('name', 'attack_priority', 'longitude', 'latitude', 'enemy_organization', 'target_goal', 'was_target_destroyed', 'target_id')

    def create(self, validated_data):
        return Target(**validated_data)
    
    def update(self, instance, validated_data):
        # Implement here an update function
        instance.name = validated_data.get('name', instance.name)
        instance.attack_priority = validated_data.get('attack_priority', instance.attack_priority)
        instance.save()
        return instance
    