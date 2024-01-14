from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework import status

# Create your views here.
@csrf_exempt
@require_http_methods(["GET"])
def get_all_employees(request):
    """
    A function that gets all employees and returns their info.
    """
    employees = Employee.objects.all()
    serializer = EmployeeSerializer(employees, many=True)
    return HttpResponse(serializer.data, status=status.HTTP_200_OK)

@csrf_exempt
@require_http_methods(["POST"])
def add_employee(request):
    """
    A function that adds a new employee to db
    """
    request_data = JSONParser().parse(request)
    serializer = EmployeeSerializer(data=request_data)
    if serializer.is_valid():
        serializer.save()
        return HttpResponse(status=status.HTTP_201_CREATED)
    return HttpResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@require_http_methods(["PUT"])
def update_employee(request, id):
    """
    a function that updates an employee with their id
    """
    request_data = JSONParser().parse(request)
    employee = Employee.objects.get(id=id)
    serializer = EmployeeSerializer(employee, data=request_data)
    if serializer.is_valid():
        employee.name = request_data["name"]
        employee.salary = request_data["salary"]
        employee.seniority = request_data["seniority"]
        employee.save()
        return HttpResponse(serializer.data, status=status.HTTP_201_CREATED)
    return HttpResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@require_http_methods(["DELETE"])
def delete_employee(request, id):
    """
    a function that removes an employee from db with their id
    """
    try:
        employee = Employee.objects.get(id=id)
    except:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    employee.delete()
    return HttpResponse(status=status.HTTP_201_CREATED)

@csrf_exempt
@require_http_methods(["GET"])
def get_employee(request, id): 
    """
    A function that gets an employee based on given id and returns it.
    """
    employee = get_object_or_404(Employee, id=id)
    serializer = EmployeeSerializer(employee)
    print(serializer.data)
    return HttpResponse(f"{serializer.data}", status=status.HTTP_200_OK)
