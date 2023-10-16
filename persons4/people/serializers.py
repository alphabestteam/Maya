from rest_framework import serializers
from .models import Person

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('name', 'person_id', 'date_of_birth', 'city')

        def create(self, validated_data):
            return Person(**validated_data)
    
        def update(self, instance, validated_data):
        # Implement here an update function
            instance.name = validated_data.get('name', instance.name)
            instance.person_id = validated_data.get('person_id', instance.person_id)
            instance.date_of_birth = validated_data.get('date_of_birth', instance.date_of_birth)
            instance.city = validated_data.get('city', instance.city)
            instance.save()
            return instance