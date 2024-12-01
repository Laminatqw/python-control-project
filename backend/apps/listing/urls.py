from django.urls import path

from .views import ListingListCreateView, ListingRetrieveUpdateDeleteView, ListingStatsView

urlpatterns = [
    path('', ListingListCreateView.as_view(), name='listings-list-create'),
    path('/<int:pk>', ListingRetrieveUpdateDeleteView.as_view(), name='listing-detail'),
    path('/<int:pk>/stats', ListingStatsView.as_view(), name='listing-stats'),
]