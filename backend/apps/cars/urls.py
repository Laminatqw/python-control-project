from django.urls import path

from .views import CarBrandListView, CarListCreateView

urlpatterns = [
    path('', CarListCreateView.as_view(), name='cars_list'),
    path('/brands', CarBrandListView.as_view(), name='cars_brands'),
]