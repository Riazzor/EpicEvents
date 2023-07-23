from rest_framework import permissions
from django.contrib.auth.models import Group


def is_in_group(user, group_name):
    try:
        return Group.objects.get(name=group_name).user_set.filter(id=user.id).exists()
    except Group.DoesNotExist:
        print(f'{group_name} does not exist')
        return False


class HasGroupPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        required_groups = view.permission_groups.get(view.action)
        if required_groups is None:
            return False
        else:
            return any([is_in_group(request.user, group_name) for group_name in required_groups])

    def has_object_permission(self, request, view, object):
        return False


class IsManagerTeam(permissions.BasePermission):
    def has_object_permission(self, request, view, object):
        if 'manager' in request.user.groups.values_list('name', flat=True):
            return True
        return False

    def has_permission(self, request, view):
        return False


class IsSalesContact(permissions.BasePermission):
    """
    Object-level permission.
    Only the sales member responsible for the corresponding customer
    can modify.
    """

    def has_object_permission(self, request, view, object):
        if object.sales_member == request.user or request.method in permissions.SAFE_METHODS:
            return True
        return False

    def has_permission(self, request, view):
        return False


class IsSupportContact(permissions.BasePermission):
    """
    Object-level permission.
    Only the support member responsible for the corresponding customer
    can modify.
    """

    def has_object_permission(self, request, view, object):
        if object.support_member == request.user or request.method in permissions.SAFE_METHODS:
            return True
        return False

    def has_permission(self, request, view):
        return False
