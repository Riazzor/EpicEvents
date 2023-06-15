from rest_framework import permissions


class IsSalesContact(permissions.BasePermission):
    """
    Only the sales member responsible for the corresponding customer
    can modify.
    """

    def has_object_permission(self, request, view, object):
        if object.sales_member == request.user:
            return True
        return False


class IsSupportContact(permissions.BasePermission):
    """
    Only the support member responsible for the corresponding customer
    can modify.
    """

    def has_object_permission(self, request, view, object):
        if object.support_member == request.user:
            return True
        return False


class IsManagerTeam(permissions.BasePermission):
    def has_object_permission(self, request, view, object):
        if 'manager' in request.user.groups:
            return True
        return False
