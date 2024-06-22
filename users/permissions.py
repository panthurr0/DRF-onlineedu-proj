from rest_framework.permissions import BasePermission


class IsModer(BasePermission):
    """Проверяет, является ли пользователь модератором."""
    message = 'Доступно только модератору'

    def has_permission(self, request, view):
        return request.user.groups.filter(name="Moder").exists()


class IsOwner(BasePermission):
    """Проверяет, является ли пользователь владельцем объекта."""
    message = 'Доступно только владельцу'

    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user
