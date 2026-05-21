from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('doc.urls'),),
    path('api/', include('users.urls'),),
    path('api/', include('converter.urls'),)
]
