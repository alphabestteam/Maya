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
        serializer = TargetSerializer(data = request_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
def update_target(request):
    # Implement here an update function
    if request.method == 'PUT':
        request_data = JSONParser().parse(request)
        serializer = TargetSerializer(data = request_data)
        pk = request_data.get('pk', None)
        target = Target.objects.get(pk=pk)
        serializer = TargetSerializer(target, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



def all_targets(request):
    # Implement here a get all targets function
    if request.method == 'GET':
        targets = Target.objects.all()
        serializer = TargetSerializer(targets, many=True)
        return JsonResponse(serializer.data, safe=False)