"""Custom permissions module"""
from rest_framework.permissions import BasePermission
from .models import Bucketlist

class IsOwner(BasePermission):
    """Custom permissions for allowing only bucketlist owners edit permissions"""

    def has_object_permission(self, request, view, obj):
        """Return True if permission is granted to bucketlist owner."""

        if isinstance(obj, Bucketlist):
            return obj.owner == request.user
        return obj.owner == request.user
