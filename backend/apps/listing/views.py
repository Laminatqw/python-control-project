from django.core.mail import send_mail
from django.db.models import Avg

from rest_framework.exceptions import ValidationError
from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    RetrieveUpdateDestroyAPIView,
    UpdateAPIView,
)
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from core.etc.record_view import record_view
from core.permissions.is_prem_user import IsPremiumUser

from apps.listing.models import ListingModel
from apps.listing.serializer import ListingSerializer, ListingStatsSerializer


# Create your views here.
class ListingListView(ListAPIView):
    serializer_class = ListingSerializer
    queryset = ListingModel.objects.all()
    permission_classes = [AllowAny,]

class ListingCreateAPIView(CreateAPIView):
    queryset = ListingModel.objects.all()
    serializer_class = ListingSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user


        if user.account_type == 'basic' and ListingModel.objects.filter(seller=user).count() >= 1:
            raise ValidationError("Basic users can only create one listing.")

        serializer.save(seller=user)

class ListingStatsView(APIView):
    permission_classes = [IsAuthenticated, IsPremiumUser]

    def get(self, request, pk):
        try:
            # Використовуємо ListingModel замість Listing
            listing = ListingModel.objects.get(pk=pk)

            # Дозвіл лише продавцям або преміум-користувачам
            if listing.seller != request.user and not request.user.is_staff:
                if request.user.account_type != 'premium':
                    return Response({'detail': 'Access denied'}, status=403)

            stats = ListingStatsSerializer.get_stats(listing)
            return Response(stats)
        except ListingModel.DoesNotExist:
            return Response({'detail': 'Listing not found'}, status=404)




class ListingDetailView(ListAPIView):
    queryset = ListingModel.objects.all()
    serializer_class = ListingSerializer
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        listing = self.get_object()

        # Фіксуємо перегляд
        print('1')
        record_view(request, listing)
        print('2')
        serializer = self.get_serializer(listing)
        return Response(serializer.data)

class NotifyAdminView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        brand = request.data.get('brand')
        if not brand:
            return Response({"detail": "Brand is required."}, status=400)


        send_mail(
            subject="New car brand request",
            message=f"User {request.user.email} requests to add the brand: {brand}.",
            from_email="no-reply@platform.com",
            recipient_list=["admin@platform.com"],
        )
        return Response({"detail": "Request sent to admin."}, status=200)


class AveragePriceView(APIView):
    def get(self, request, region=None):
        queryset = ListingModel.objects.filter(status='active')
        if region:
            queryset = queryset.filter(region=region)

        avg_price = queryset.aggregate(Avg('price'))['price__avg']
        return Response({'average_price': avg_price or 0})