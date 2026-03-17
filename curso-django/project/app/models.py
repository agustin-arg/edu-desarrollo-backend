from django.db import models

class Car(models.Model):
    title = models.TextField(max_length=250)
