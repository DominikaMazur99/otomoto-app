from django.db import models

class Car(models.Model):
    car_name = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    fuel_type = models.CharField(max_length=50)
    mileage = models.IntegerField()  # Assuming it's an integer field
    price = models.IntegerField(null=True,blank=True)
    year = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.car_name
