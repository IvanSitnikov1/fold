from rest_framework import permissions


class IsProvider(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if user.is_authenticated and user.user_type == 'provider':
            return True
        return False


class IsConsumer(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if user.is_authenticated and user.user_type == 'consumer':
            return True
        return False