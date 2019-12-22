from django.db import models
from model_utils import Choices
# Create your models here.


class Engine(models.Model):
    ENGINE_TYPES = Choices("benz","diesel","electric")
    capacity = models.IntegerField(blank=True, null=True)
    power = models.IntegerField()
    typ = models.CharField(max_length=20, choices=ENGINE_TYPES)
    name = models.CharField(max_length=255)

class Car(models.Model):
    engine = models.ForeignKey("cars.Engine", on_delete=models.CASCADE)
    model = models.CharField(max_length=200)
    mark = models.CharField(max_length=200)
    year = models.IntegerField()
    image = models.ImageField(blank=True, null=True, upload_to='car_images/%Y/%m/%d/')
