from rest_framework.permissions import SAFE_METHODS, BasePermission


class RegisterPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method != 'GET':
            return True
