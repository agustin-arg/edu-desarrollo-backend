import os
import uuid
from django.db import models
from django.core.exceptions import ValidationError
from convert_files.users import User


def user_directory_path(instance, filename):
    file_extension = os.path.splitext(filename)[1].lstrip(".").lower()
    unique_filename = f"{uuid.uuid4().hex}_{filename}"
    return os.path.join(
        "media", instance.user.username, file_extension, unique_filename
    )


class File(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="files")
    original_name = models.CharField(max_length=128, editable=False)
    name = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    file_path = models.FileField(upload_to=user_directory_path, editable=False)
    size_bytes = models.BigIntegerField(editable=False)
    mime_type = models.CharField(max_length=50)
    uploaded_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "File"
        verbose_name_plural = "Files"
        constraints = [
            models.UniqueConstraint(
                fields=["user", "name"],
                name="unique_file_per_user",
            )
        ]

    def __str__(self):
        return f"{self.name} ({self.user.username})"


class Format(models.Model):
    extension = models.CharField(unique=True, max_length=5)
    category = models.CharField(max_length=20)
    is_active = models.BooleanField(default=True)


class ConvertFormat(models.Model):
    original_extension = models.ForeignKey(
        Format, on_delete=models.CASCADE, related_name="original_conversions"
    )
    output_extension = models.ForeignKey(
        Format, on_delete=models.CASCADE, related_name="output_conversions"
    )
    is_active = models.BooleanField(default=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["original_extension", "output_extension"],
                name="unique_convert_format",
            )
        ]
        verbose_name = "Convert Format"
        verbose_name_plural = "Convert Formats"


class Task(models.Model):
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("processing", "Processing"),
        ("completed", "Completed"),
        ("failed", "Failed"),
    ]

    file = models.ForeignKey(File, on_delete=models.CASCADE, related_name="tasks")
    conversion = models.ForeignKey(
        ConvertFormat, on_delete=models.CASCADE, related_name="tasks"
    )
    status = models.CharField(
        max_length=20,
        default="pending",
        choices=STATUS_CHOICES,
    )
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    finished_at = models.DateTimeField(editable=False, null=True, blank=True)
    error_message = models.CharField(
        max_length=255, editable=False, null=True, blank=True
    )

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Task"
        verbose_name_plural = "Tasks"
