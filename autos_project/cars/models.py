from django.db import models

class Car(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=50)
    license_plate = models.CharField(max_length=20, unique=True)
    year = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name} ({self.license_plate})"
