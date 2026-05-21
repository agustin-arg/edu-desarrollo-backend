from rest_framework.routers import DefaultRouter

from .views import FileViewSet, TaskViewSet, ConvertFormatViewSet, FormatViewSet

router = DefaultRouter()
router.register("file", FileViewSet)
router.register("task", TaskViewSet)
router.register("convert", ConvertFormatViewSet)
router.register("format", FormatViewSet)

urlpatterns = router.urls
