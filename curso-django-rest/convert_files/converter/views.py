from .models import File, Task, ConvertFormat, Format
from .serializers import FileSerializer, TaskSerializer, ConvertFormatSerializer, FormatSerializer
from rest_framework.viewsets import ModelViewSet

class FileViewSet(ModelViewSet):
    serializer_class = FileSerializer
    queryset = File.objects.all()
    lookup_field = "id"

class TaskViewSet(ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    lookup_field = "id"

class ConvertFormatViewSet(ModelViewSet):
    serializer_class = ConvertFormatSerializer
    queryset = ConvertFormat.objects.all()
    lookup_field = "id"

class FormatViewSet(ModelViewSet):
    serializer_class = FormatSerializer
    queryset = Format.objects.all()
    lookup_field = "id"

    
