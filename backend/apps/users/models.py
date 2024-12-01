from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from core.models import BaseModel

from .manager import UserManager

ROLES = (
    ('buyer', 'Buyer'),
    ('seller', 'Seller'),
    ('manager', 'Manager'),
    ('admin', 'Administrator'),
)

ACCOUNT_TYPES = (
    ('basic', 'Basic'),
    ('premium', 'Premium'),
)

# Create your models here.
class UserModel(AbstractBaseUser, PermissionsMixin, BaseModel):
    class Meta:
        db_table = 'auth_user'

    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    role = models.CharField(max_length=20, choices=ROLES, default='buyer')
    account_type = models.CharField(max_length=10, choices=ACCOUNT_TYPES, default='basic')
    USERNAME_FIELD = 'email'
    objects = UserManager()


class ProfileModel(BaseModel):
    class Meta:
        db_table = 'profile'

    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    age = models.IntegerField()
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE, related_name='profile')