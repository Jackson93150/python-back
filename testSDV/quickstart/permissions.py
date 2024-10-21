from rest_framework import permissions

class IsAdmin(permissions.BasePermission):
    """
    Permission for users in the Admin group.
    Allows all actions.
    """
    def has_permission(self, request, view):
        return request.user and request.user.groups.filter(name='Admin').exists()

class IsViewer(permissions.BasePermission):
    """
    Permission for users in the Viewer group.
    Allows only read actions.
    """
    def has_permission(self, request, view):
        return request.user and request.user.groups.filter(name='Viewer').exists()

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Permission to only allow owners of an object to edit it.
    """
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed for any request.
        if request.method in permissions.SAFE_METHODS:
            return True
        # Write permissions are only allowed to the owner of the object.
        return obj.user == request.user
