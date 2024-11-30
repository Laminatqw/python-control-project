from django.db import models

from core.models import BaseModel

# from cars.services import upload_car_photo


# Create your models here.

class CarModel(BaseModel):
    class Meta:
        db_table = 'cars'
    # seller_id = models.ForeignKey()
    CURRENCY_CHOICES = [
        ('UAH', 'Українська гривня'),
        ('EUR', 'Євро'),
        ('USD', 'Долар США'),
    ]

    STATUS_CHOICES = [
        ('active', 'Активний'),
        ('inactive', 'Неактивний'),
        ('pending', 'На розгляді'),
    ]
    model = models.CharField(max_length=25)
    brand = models.CharField(max_length=25)
    price = models.IntegerField()
    region = models.CharField(max_length=25)
    currency = models.CharField(max_length=5, choices=CURRENCY_CHOICES, default='EUR')
    status = models.CharField(max_length=25, choices=STATUS_CHOICES, default='active')



    # salon
    # photo = models.ImageField(upload_to= upload_car_photo, blank=True)