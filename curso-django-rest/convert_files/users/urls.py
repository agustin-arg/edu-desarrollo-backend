from django.urls import path
from .views import list_users, detail_user

urlpatterns = [
    path('users/', list_users),
    path('users/<int:pk>', detail_user)
]
