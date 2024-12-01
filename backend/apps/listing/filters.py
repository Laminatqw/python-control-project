from datetime import timedelta

from django.db.models import Avg
from django.utils.timezone import now

import django_filters

from .models import ListingModel


def get_listing_stats(listing, region):
    """
    Розраховує статистику для конкретного оголошення.

    Args:
        listing (Listing): Оголошення, для якого розраховується статистика.
        region (str): Регіон, в якому знаходиться оголошення.

    Returns:
        dict: Статистика у вигляді словника.
    """
    today = now().date()  # Поточна дата
    week_ago = today - timedelta(days=7)  # Дата тиждень тому

    # Кількість переглядів за сьогодні
    views_today = listing.views.filter(viewed_at__date=today).count()

    # Кількість переглядів за останній тиждень
    views_week = listing.views.filter(viewed_at__date__gte=week_ago).count()

    # Середня ціна по регіону
    avg_price_region = ListingModel.objects.filter(region=region).aggregate(Avg('price'))['price__avg']

    # Середня ціна по країні
    avg_price_country = ListingModel.objects.aggregate(Avg('price'))['price__avg']

    return {
        'views_today': views_today,
        'views_week': views_week,
        'avg_price_region': avg_price_region or 0,  # Якщо немає даних, повертаємо 0
        'avg_price_country': avg_price_country or 0,
    }

class ListingFilter(django_filters.FilterSet):
    price_min = django_filters.NumberFilter(field_name="price", lookup_expr='gte')
    price_max = django_filters.NumberFilter(field_name="price", lookup_expr='lte')
    region = django_filters.CharFilter(field_name="region", lookup_expr='icontains')
    make = django_filters.CharFilter(field_name="car__make__name", lookup_expr='icontains')
    model = django_filters.CharFilter(field_name="car__model__name", lookup_expr='icontains')



    class Meta:
        model = ListingModel
        fields = ['region', 'make', 'model', 'price_min', 'price_max']
