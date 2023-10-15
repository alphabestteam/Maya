from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from targets.models import Target
from targets.serializers import TargetSerializer
from rest_framework import status

@csrf_exempt
def add_target(request):
    # Implement here an add function
    if request.method == 'POST':
        request_data = JSONParser().parse(request)
        target = Target(
            name=request_data["name"],
            attack_priority=request_data["attack_priority"],
            longitude=request_data["longitude"],
            latitude=request_data["latitude"],
            enemy_organization=request_data["enemy_organization"],
            target_goal=request_data["target_goal"],
            was_target_destroyed=request_data["was_target_destroyed"],
            target_id=request_data["target_id"]
        )
        serializer = TargetSerializer(data = request_data)
        if serializer.is_valid():
            target.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
def update_target(request):
    # Implement here an update function
    if request.method == 'PUT':
        request_data = JSONParser().parse(request)
        print(request_data)
        pk = request_data.get('target_id', None)
        target = Target.objects.get(target_id=pk)
        serializer = TargetSerializer(target, data=request_data)
        if serializer.is_valid():
            target.name = request_data["name"]
            target.attack_priority = request_data["attack_priority"]
            target.longitude = request_data["longitude"]
            target.latitude = request_data["latitude"]
            target.enemy_organization = request_data["enemy_organization"]
            target.target_goal = request_data["target_goal"]
            target.was_target_destroyed = request_data["was_target_destroyed"]
            target.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



def all_targets(request):
    # Implement here a get all targets function
    if request.method == 'GET':
        targets = Target.objects.all()
        serializer = TargetSerializer(targets, many=True)
        return JsonResponse(serializer.data, safe=False)