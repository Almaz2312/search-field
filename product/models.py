from django.db import models
from django.forms import CharField


# Create your models here.
class Manufacturer(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return self.name
