from rest_framework import serializers
from .models import Trip, RequestedTrip

class TripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = '__all__'


class RequestedTripSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestedTrip
        fields = '__all__'