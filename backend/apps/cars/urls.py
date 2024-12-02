from django.urls import path

from .views import CarBrandListView, CarListCreateView, NotifyAdminView

urlpatterns = [
    path('', CarListCreateView.as_view(), name='cars_list'),
    path('/brands', CarBrandListView.as_view(), name='cars_brands'),
    path('/report', NotifyAdminView.as_view(), name='cars_report'),
]