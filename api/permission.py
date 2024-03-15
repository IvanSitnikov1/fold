from rest_framework import permissions


class IsProvider(permissions.BasePermission):
    """Разрешения для поставщика"""
    def has_permission(self, request, view):
        user = request.user
        if user.is_authenticated and user.user_type == 'provider':
            return True
        return False


class IsConsumer(permissions.BasePermission):
    """Разрешения для потребителя"""
    def has_permission(self, request, view):
        user = request.user
        if user.is_authenticated and user.user_type == 'consumer':
            return True
        return False
