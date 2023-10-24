from django.urls import path
from . import views

urlpatterns = [
    path('getAllUsers/', views.ListUsers.as_view(), name='list_users'),
    path('addUser/', views.ListUsers.as_view(), name='list_users'),
    path('updateUser/', views.ListUsers.as_view(), name='list_users'),
    path('deleteUser/<int:user_id>/', views.ListUsers.as_view(), name='user_id'),
]