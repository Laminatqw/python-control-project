from rest_framework import serializers

from apps.cars.models import CarModel


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = ['id', 'brand', 'model']

    def create(self, validated_data):
        # Додаємо продавця (seller) з контексту
        validated_data['seller'] = self.context['request'].user
        return super().create(validated_data)

