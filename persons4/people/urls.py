from django.urls import path
from . import views

urlpatterns = [
    path('getAllPeople/', views.get_people),
    path('addPerson/', views.add_person),
    path('removePerson/<int:person_id>/', views.remove_person, name='person_id'),
    path('updatePerson/', views.update_person),
]