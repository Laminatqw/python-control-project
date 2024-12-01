from rest_framework import serializers

from apps.cars.serializer import CarSerializer
from apps.listing.models import ListingModel, ListingViewModel


class ListingSerializer(serializers.ModelSerializer):
    car = CarSerializer()  # Вкладений серіалізатор для машини

    class Meta:
        model = ListingModel
        fields = ['id', 'price', 'currency', 'region', 'status', 'car']

    def create(self, validated_data):
        # Витягуємо дані машини
        car_data = validated_data.pop('car')

        # Передаємо `context` для доступу до `request.user`
        car_serializer = CarSerializer(data=car_data, context=self.context)
        car_serializer.is_valid(raise_exception=True)
        car = car_serializer.save()  # Створюємо об'єкт Car

        # Створюємо оголошення, пов'язане з машиною
        validated_data['seller'] = self.context['request'].user
        validated_data['car'] = car
        return super().create(validated_data)


class ListingViewSerializer(serializers.ModelSerializer):
    model = ListingViewModel
    fields = ('listing', 'viewed_at', 'region')

class ListingStatsSerializer(serializers.Serializer):
    views_today = serializers.IntegerField()  # Кількість переглядів за сьогодні
    views_week = serializers.IntegerField()   # Кількість переглядів за останній тиждень
    avg_price_region = serializers.DecimalField(max_digits=10, decimal_places=2)  # Середня ціна по регіону
    avg_price_country = serializers.DecimalField(max_digits=10, decimal_places=2) # Середня ціна по всій країні
