from rest_framework import serializers
from .models import Person, Parent

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'

    def create(self, validated_data):
        return Person.objects.create(**validated_data)

    def update(self, instance, validated_data):
    # Implement here an update function
        instance.name = validated_data.get('name', instance.name)
        instance.person_id = validated_data.get('person_id', instance.person_id)
        instance.date_of_birth = validated_data.get('date_of_birth', instance.date_of_birth)
        instance.city = validated_data.get('city', instance.city)
        instance.save()
        return instance
        
class ParentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parent
        fields = '__all__'


class GetParentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parent
        fields = ['person']