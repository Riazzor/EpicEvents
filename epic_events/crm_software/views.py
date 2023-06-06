from rest_framework import mixins, viewsets
from django.contrib.auth import get_user_model

from . import mixins as mx, models, permissions, serializers

User = get_user_model()


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
    http_method_names = ['get', 'post', 'patch', 'head', 'options']


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
    # name email last_name and date_created of the contract can be used for query params search
    queryset_search_field = ('last_name', 'email', 'date_created', 'amount')

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


class CustomerViewSet(mx.OrObjectPermissionMixin, mx.QuerysetFilterMixin, CustomModelViewSet):
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
    # name and email of the customer can be used for query params search
    queryset_search_field = ('last_name', 'email',)

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.action == 'list':
            queryset = self.query_filter(queryset)
        return queryset

    def update(self, request, *args, **kwargs):
        print('update')
        return super().update(request, *args, **kwargs)


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
    # name email and date_created of the event can be used for query params search
    queryset_search_field = ('last_name', 'email', 'date_created')

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
