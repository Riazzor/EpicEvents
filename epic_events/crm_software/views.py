from rest_framework import mixins, viewsets

from . import mixins as mx, models, permissions, serializers


class CustomModelViewSet(
        mixins.CreateModelMixin,
        mixins.RetrieveModelMixin,
        mixins.UpdateModelMixin,
        mixins.ListModelMixin,
        viewsets.GenericViewSet,
):
    """
    Custom model viewsets without the destroy mixin
    """
    pass


class ContractViewSet(mx.OrObjectPermissionMixin, CustomModelViewSet):
    queryset = models.Contract.objects.all()
    serializer_class = serializers.ContractSerializer
    permission_classes = (
        permissions.IsSalesContact, permissions.HasGroupPermission, permissions.IsManagerTeam
    )
    permission_groups = {  # only for group level permissions
        'retrieve': ['manager', 'sales', 'support'],
        'list': ['manager', 'sales', 'support'],
        'create': ['manager', 'sales'],
        'destroy': None,
        'update': ['manager'],
        'partial_update': ['manager'],
    }


class CustomerViewSet(mx.OrObjectPermissionMixin, CustomModelViewSet):
    queryset = models.Customer.objects.all()
    serializer_class = serializers.CustomerSerializer
    permission_classes = (
        permissions.IsSalesContact, permissions.HasGroupPermission, permissions.IsManagerTeam
    )
    permission_groups = {  # only for group level permissions
        'retrieve': ['manager', 'sales', 'support'],
        'list': ['manager', 'sales', 'support'],
        'create': ['manager', 'sales'],
        'destroy': None,
        'update': ['manager'],
        'partial_update': ['manager'],
    }


class EventViewSet(mx.OrObjectPermissionMixin, CustomModelViewSet):
    queryset = models.Events.objects.all()
    serializer_class = serializers.EventSerializer
    permission_classes = (
        permissions.IsSalesContact,
        permissions.HasGroupPermission,
        permissions.IsManagerTeam,
        permissions.IsSupportContact,
    )
    permission_groups = {  # only for group level permissions
        'retrieve': ['manager', 'sales', 'support'],
        'list': ['manager', 'sales', 'support'],
        'create': ['manager', 'sales'],
        'destroy': None,
        'update': ['manager'],
        'partial_update': ['manager'],
    }
