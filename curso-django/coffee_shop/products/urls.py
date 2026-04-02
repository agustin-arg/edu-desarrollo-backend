from django.urls import path
from .views import ProductFormView

urlpatterns = [
    path("add/", ProductFormView.as_view()),
]
