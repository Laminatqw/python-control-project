from django.conf import settings
from django.db import models

from apps.cars.models import CarModel


class ListingModel(models.Model):

    seller = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='listings')
    car = models.ForeignKey(CarModel, on_delete=models.CASCADE, related_name='listings')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3, choices=[('USD', 'USD'), ('EUR', 'EUR'), ('UAH', 'UAH')])
    region = models.CharField(max_length=100)
    status = models.CharField(max_length=10, choices=[('active', 'Active'), ('inactive', 'Inactive')], default='inactive')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.car.model} - {self.price} {self.currency}"


class ListingViewModel(models.Model):
    listing = models.ForeignKey(ListingModel, on_delete=models.CASCADE, related_name='views')
    viewed_at = models.DateTimeField(auto_now_add=True)
    region = models.CharField(max_length=100)

    def __str__(self):
        return f"View for {self.listing} in {self.region}"

