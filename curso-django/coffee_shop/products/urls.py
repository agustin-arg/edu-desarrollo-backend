from django.urls import path
from .views import ProductFormView, ProductListView, ProductTableView

urlpatterns = [
    path("add/", ProductFormView.as_view(), name="add_product"),
    path("table/", ProductTableView.as_view(), name="table_product"),
    path("list/", ProductListView.as_view(), name="list_product"),
]
