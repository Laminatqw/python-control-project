from datetime import timedelta, timezone

from django.utils.timezone import now

from rest_framework import serializers

from apps.cars.serializer import CarSerializer
from apps.listing.models import ListingModel, ListingViewModel


def contains_profanity(text):
    return any(word in text.lower() for word in BAD_WORDS)


class ListingSerializer(serializers.ModelSerializer):
    car = CarSerializer()  # Вкладений серіалізатор для машини

    class Meta:
        model = ListingModel
        fields = ['id', 'description', 'price', 'currency', 'region', 'status', 'car']

    def validate_description(self, value):
        if contains_profanity(value):
            raise serializers.ValidationError("Description contains prohibited words.")
        return value
    def validate(self, data):
        if self.instance and self.instance.edit_attempts >= self.instance.max_edit_attempts:
            raise serializers.ValidationError("You cannot edit this listing more than 3 times.")
        return data

    def update(self, instance, validated_data):
        instance.edit_attempts += 1
        return super().update(instance, validated_data)


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
    total_views = serializers.IntegerField()
    daily_views = serializers.IntegerField()
    weekly_views = serializers.IntegerField()

    @staticmethod
    def get_stats(listing):
        today = now().date()
        week_ago = today - timedelta(days=7)

        total_views = listing.views.count()
        daily_views = listing.views.filter(viewed_at__date=today).count()
        weekly_views = listing.views.filter(viewed_at__date__gte=week_ago).count()

        return {
            'total_views': total_views,
            'daily_views': daily_views,
            'weekly_views': weekly_views,
        }

BAD_WORDS = ['badword1', 'badword2', 'badword3']




