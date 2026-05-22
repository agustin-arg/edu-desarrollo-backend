from django.contrib import admin
from django.urls import path, include
import rest_framework

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('doc.urls'),),
    path('api/', include('users.urls'),),
    path('api/', include('converter.urls'),),
    path('api-auth', include('rest_framework.urls'))
]
