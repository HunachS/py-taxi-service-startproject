from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(unique=True)
    country = models.CharField()

    def __str__(self):
        return self.name


class Car(models.Model):
    model = models.CharField()
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, related_name="cars")
    drivers = models.ManyToManyField(settings.AUTH_USER_MODEL)

    def __str__(self):
        return f"{self.manufacturer.name} {self.model}"

class Driver(AbstractUser):
    license_number = models.CharField(unique=True)

    class Meta:
        verbose_name = "driver"
        verbose_name_plural = "drivers"
