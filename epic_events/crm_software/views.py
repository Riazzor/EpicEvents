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

    def get_queryset(self):
        queryset = super().get_queryset()
        customer = self.request.query_params.get('customer', None)
        sales_member = self.request.query_params.get('sales_member', None)
        if self.action == 'list':
            if customer:
                queryset = queryset.filter(customer__first_name__icontains=customer)
            if sales_member:
                queryset = queryset.filter(sales_member__first_name__icontains=sales_member)
        return queryset


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

    def get_queryset(self):
        queryset = super().get_queryset()
        sales_member = self.request.query_params.get('sales_member', None)
        if self.action == 'list':
            if sales_member:
                queryset = queryset.filter(sales_member__first_name__icontains=sales_member)
        return queryset


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

    def get_queryset(self):
        queryset = super().get_queryset()
        customer = self.request.query_params.get('customer', None)
        support_member = self.request.query_params.get('support_member', None)
        if self.action == 'list':
            if customer:
                queryset = queryset.filter(customer__first_name__icontains=customer)
            if support_member:
                queryset = queryset.filter(sales_member__first_name__icontains=support_member)
        return queryset
