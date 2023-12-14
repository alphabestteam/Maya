from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', views.UserViewSet)
urlpatterns = [
    path('register/', include(router.urls)),
#     path('addPerson/', views.add_person),
#     path('removePerson/<int:person_id>/', views.remove_person, name='person_id'),
#     path('updatePerson/', views.update_person),
#     path('getAllParents/', views.get_parents),
#     path('addParent/', views.add_parent),
#     path('updateParent/', views.update_parent),
#     path('removeParent//', ),
#     path('connectKidToParent/', views.api_connect_kid_parent),
#     path('getParent/', views.api_get_parent),
#     path('getRichKids/', views.find_rich_kids),
#     path('getParentsNames/<int:person_id>/', views.get_parents_names, name='get_parents_names'),
#     path('getKids/', views.get_kids),
#     path('getGrandParents/', views.get_grandparents),
#     path('getSiblings/', views.find_siblings),
]