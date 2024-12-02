from django.urls import path

from .views import AveragePriceView, ListingCreateAPIView, ListingDetailView, ListingListView, ListingStatsView

urlpatterns = [
    path('', ListingListView.as_view(), name='listings-list'),

    path('/create', ListingCreateAPIView.as_view(), name='listings-create'),
    path('/<int:pk>', ListingDetailView.as_view(), name='listing-detail'),
    path('/<int:pk>/stats', ListingStatsView.as_view(), name='listing-stats'),
    path('/average', AveragePriceView.as_view(), name='listing-average'),
]