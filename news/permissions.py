from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import BasePermission
from rest_framework import permissions


class IsAuthorOrIsAuthenticated(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return bool(request.user and request.user.is_authenticated)
        return obj.author == request.user


class IsActive(BasePermission):
    def has_permission(self, request, view):
        try:
            request.user.is_active
        except:
            raise PermissionDenied('You do not have access rights')
        return bool(request.user and request.user.is_active)
