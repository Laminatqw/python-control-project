from django.contrib.auth import get_user_model
from django.db.transaction import atomic

from rest_framework import serializers

from apps.users.models import ProfileModel

# from core.services.email_service import EmailService


UserModel = get_user_model()

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileModel
        fields = ('id',
                  'name',
                  'surname',
                  'age',
                  'created_at',
                  'updated_at'
                  )


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(required=False)  # Робимо profile необов'язковим

    class Meta:
        model = UserModel
        fields = (
            'id', 'email', 'password', 'is_active', 'is_staff',
            'is_superuser', 'last_login', 'created_at', 'updated_at', 'profile'
        )
        read_only_fields = ('id', 'is_active', 'is_staff', 'is_superuser', 'last_login', 'created_at', 'updated_at')
        extra_kwargs = {
            'password': {'write_only': True},
        }

    @atomic
    def create(self, validated_data: dict):
        profile_data = validated_data.pop('profile', None)
        user = UserModel.objects.create_user(**validated_data)
        validated_data['is_active'] = True
        if profile_data:
            ProfileModel.objects.create(user=user, **profile_data)
        return user
