from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    # Add here the targets URL
    path('api/targets/', include('targets.urls'))
]
