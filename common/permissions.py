from rest_framework import permissions


class BasePermission(permissions.BasePermission):
    """ BasePermission class adds all permissions for superUsers """

    def has_object_permission(self, request, view, obj):
        return bool(request.user and request.user.is_superuser)

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_superuser)


class IsSuperUser(BasePermission):
    """Allows access only to superusers."""

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_superuser)
