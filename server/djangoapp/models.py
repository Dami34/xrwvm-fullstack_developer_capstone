from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    
    def __str__(self):
        return self.name

class CarModel(models.Model):
    CAR_TYPES = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
        ('TRUCK', 'Truck'),
        ('COUPE', 'Coupe')
    ]
    
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    dealer_id = models.IntegerField()
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=10, choices=CAR_TYPES, default='SUV')
    year = models.IntegerField(
        validators=[
            MaxValueValidator(2023),
            MinValueValidator(2015)
        ]
    )
    
    def __str__(self):
        return f"{self.car_make.name} {self.name} ({self.year})"

from django.contrib import admin
from .models import CarMake, CarModel

admin.site.register(CarMake)
admin.site.register(CarModel)