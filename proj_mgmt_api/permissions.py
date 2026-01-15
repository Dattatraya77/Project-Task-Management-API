from rest_framework.permissions import BasePermission


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated and request.user.profile.role == "admin"
        )


class IsManagerOrIsAdmin(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated and request.user.profile.role in ["admin", "manager"]
        )


class IsUserOrAbove(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated