from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'forms', views.FormViewSet)
router.register(r'sharedForm', views.SharedViewSet)
router.register(r'messageForm', views.MessagesViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
] 