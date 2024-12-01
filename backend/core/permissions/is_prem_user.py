from rest_framework.permissions import BasePermission


class IsPremiumUser(BasePermission):
    def has_permission(self, request, view):
        return request.user.account_type == 'premium'