from rest_framework import permissions
from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user


class IsOwnerOrPostOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        # Allow POST requests from any user
        if request.method == 'POST':
            return True
        # Allow GET, HEAD or OPTIONS requests (SAFE_METHODS)
        elif request.method in permissions.SAFE_METHODS:
            return True
        # Otherwise, only the owner can edit the object
        return obj.user == request.user
