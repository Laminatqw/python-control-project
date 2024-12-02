from django.conf import settings
from django.db import models

from apps.cars.models import CarModel


class ListingModel(models.Model):

    seller = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='listings')
    car = models.ForeignKey(CarModel, on_delete=models.CASCADE, related_name='listings')
    description = models.TextField(max_length=500)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3, choices=[('USD', 'USD'), ('EUR', 'EUR'), ('UAH', 'UAH')])
    region = models.CharField(max_length=100)
    status = models.CharField(max_length=10, choices=[('active', 'Active'), ('inactive', 'Inactive')], default='active')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    edit_attempts = models.IntegerField(default=0)
    max_edit_attempts = 3

    def __str__(self):
        return f"{self.car.model} - {self.price} {self.currency}"





class ListingViewModel(models.Model):
    listing = models.ForeignKey(
        ListingModel,
        on_delete=models.CASCADE,
        related_name='views'
    )
    viewer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='viewed_listings'
    )
    viewed_at = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)  # Для унікальності

    def __str__(self):
        return f"View on {self.listing} by {self.viewer or 'Anonymous'} at {self.viewed_at}"
