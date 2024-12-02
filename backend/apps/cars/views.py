from django.shortcuts import render

from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from core.etc.notify_admin import notify_admin_about_new_brand

from apps.cars.models import CarModel
from apps.cars.serializer import CarSerializer


# Create your views here.
class CarListCreateView(ListCreateAPIView):
    serializer_class = CarSerializer
    queryset = CarModel.objects.all()

class CarDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = CarSerializer
    queryset = CarModel.objects.all()

class CarBrandListView(ListAPIView):
    queryset = CarModel.objects.values_list('brand', flat=True).distinct()

    def list(self, request, *args, **kwargs):
        brands = self.get_queryset()
        return Response({'brands': list(brands)})


    class NotifyAdminView(APIView):
        permission_classes = [IsAuthenticated]

        def post(self, request):
            brand = request.data.get('brand')
            if not brand:
                return Response({"detail": "Brand is required."}, status=400)

            notify_admin_about_new_brand(request.user, brand)
            return Response({"detail": "Request sent to admin."}, status=200)
