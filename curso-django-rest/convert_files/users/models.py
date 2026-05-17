from django.db import models


class User(models.Model):
    username = models.CharField(unique=True, max_length=128)
    email = models.EmailField(unique=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
    password = models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        ordering = ["username"]
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return self.username
