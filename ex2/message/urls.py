from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'message', views.MessageViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
] 