from django.urls import path, include
from . import views

#urls
urlpatterns = [
    path('getAllEmployees/', views.get_all_employees),
    path('addEmployee/', views.add_employee),
    path('updateEmployee/<int:id>/', views.update_employee, name='id'),
    path('deleteEmployee/<int:id>/', views.delete_employee, name='id'),
    path('getEmployee/<int:id>/', views.get_employee, name='id'),
]