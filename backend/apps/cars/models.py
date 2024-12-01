from django.db import models

from core.models import BaseModel

from config import settings

# from cars.services import upload_car_photo


# Create your models here.

class CarModel(BaseModel):
    class Meta:
        db_table = 'cars'

    seller = models.ForeignKey(
        settings.AUTH_USER_MODEL,  # Зв'язок із користувачем
        on_delete=models.CASCADE,
        related_name='cars'
    )
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.brand} {self.model} (Seller: {self.seller.email})"


    # salon
    # photo = models.ImageField(upload_to= upload_car_photo, blank=True)