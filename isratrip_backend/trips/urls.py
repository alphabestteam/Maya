from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', views.RequestedTripViewSet)
urlpatterns = [
    path('view-trips/', views.ListTrips.as_view()),
    path('request-new-trip/', include(router.urls))
]