from django.shortcuts import render

from rest_framework.generics import ListCreateAPIView

from apps.cars.models import CarModel
from apps.cars.serializer import CarSerializer


# Create your views here.
class CarListCreateView(ListCreateAPIView):
    serializer_class = CarSerializer
    queryset = CarModel.objects.all()
