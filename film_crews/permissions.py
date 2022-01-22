from rest_framework.permissions import BasePermission


class OnlyAuthorized(BasePermission):
    """
    Разрешает доступ только авторизованным пользователям.
    """

    def has_permission(self, request, view):
        return request.user.is_anonymous
