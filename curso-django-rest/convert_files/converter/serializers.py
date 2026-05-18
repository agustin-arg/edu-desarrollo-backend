from rest_framework import serializers

from converter.models import ConvertFormat, File, Format, Task


class FormatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Format
        fields = "__all__"


class ConvertFormatSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConvertFormat
        fields = "__all__"


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = "__all__"


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"
