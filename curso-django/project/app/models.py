from django.db import models

class Car(models.Model):
    title = models.TextField(max_length=250)
    year = models.TextField(max_length=4, null=True)