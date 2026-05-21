from django.urls import path
from .views import FileViewSet, TaskViewSet, ConvertFormatViewSet, FormatViewSet

urlpatterns = [
    path("file/", FileViewSet.as_view({"get": "list", "post": "create"})),
    path(
        "file/<int:id>/",
        FileViewSet.as_view(
            {
                "get": "retrieve",
                "put": "update",
                "patch": "partial_update",
                "delete": "destroy",
            }
        ),
    ),
    path("task/", TaskViewSet.as_view({"get": "list", "post": "create"})),
    path(
        "task/<int:id>/",
        TaskViewSet.as_view(
            {
                "get": "retrieve",
                "put": "update",
                "patch": "partial_update",
                "delete": "destroy",
            }
        ),
    ),
    path("convert/", ConvertFormatViewSet.as_view({"get": "list", "post": "create"})),
    path(
        "convert/<int:id>/",
        ConvertFormatViewSet.as_view(
            {
                "get": "retrieve",
                "put": "update",
                "patch": "partial_update",
                "delete": "destroy",
            }
        ),
    ),
    path("format/", FormatViewSet.as_view({"get": "list", "post": "create"})),
    path(
        "format/<int:id>/",
        FormatViewSet.as_view(
            {
                "get": "retrieve",
                "put": "update",
                "patch": "partial_update",
                "delete": "destroy",
            }
        ),
    ),
]
