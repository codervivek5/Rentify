from django.db import models
from django.contrib.auth.models import User

class Property(models.Model):
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    place = models.CharField(max_length=100)
    area = models.DecimalField(max_digits=10, decimal_places=2)
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    nearby_hospitals = models.CharField(max_length=255)
    nearby_colleges = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    amenities = models.TextField()
    likes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.place} - {self.area} sqft"

class Interest(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    buyer = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.buyer} interested in {self.property}"
