

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from core.permissions.is_prem_user import IsPremiumUser

from django_filters.rest_framework import DjangoFilterBackend

from apps.listing.filters import ListingFilter
from apps.listing.models import ListingModel, ListingViewModel
from apps.listing.serializer import ListingSerializer, ListingStatsSerializer, ListingViewSerializer

from .filters import get_listing_stats


# Create your views here.
class ListingListCreateView(ListCreateAPIView):
    serializer_class = ListingSerializer
    queryset = ListingModel.objects.all()

class ListingRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    serializer_class = ListingSerializer
    queryset = ListingModel.objects.all()
    permission_classes = [IsAuthenticated,]


class ListingStatsView(APIView):
    permission_classes = [IsAuthenticated, IsPremiumUser]
    filter_backends = [DjangoFilterBackend]
    filterset_class = ListingFilter



    def get(self, request, listing_id):
        try:
            listing = ListingModel.objects.get(id=listing_id)

            # Перевірка, чи користувач є власником оголошення
            if listing.seller != request.user:
                return Response({'error': 'Access denied'}, status=403)

            stats = get_listing_stats(listing, listing.region)
            return Response(ListingStatsSerializer(stats).data)
        except ListingModel.DoesNotExist:
            return Response({'error': 'Listing not found'}, status=404)

class ListingViewSet(ModelViewSet):
    queryset = ListingModel.objects.all()
    serializer_class = ListingSerializer
    permission_classes = [IsAuthenticated]  # Тільки автентифіковані користувачі

    def perform_create(self, serializer):
        # Автоматично додаємо продавця
        serializer.save(seller=self.request.user)