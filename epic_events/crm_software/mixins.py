class OrObjectPermissionMixin:
    """
    Overwrite method to implement an OR behaviour since the bitwise OR doesn't work
    since at least 2020 and no one seems to consider this bug as a MAJOR SECURITY
    RISK.
    """

    def check_permissions(self, request):
        permitted = False
        for permission in self.get_permissions():
            if permission.has_permission(request, self):
                permitted = True
        if not permitted:
            self.permission_denied(
                request,
                message='Permission denied. Ask the manager team for more details.',
            )

    def check_object_permissions(self, request, obj):
        permitted = False
        for permission in self.get_permissions():
            if permission.has_object_permission(request, self, obj):
                permitted = True
        if not permitted:
            self.permission_denied(
                request,
                message='Permission denied. Ask the manager team for more details.',
            )


class QuerysetFilterMixin:
    queryset_search_field = None

    def query_filter(self, queryset):
        for field, value in self.request.query_params.items():
            if field in self.queryset_search_field:
                filter_args = {f"{field}__icontains": value}
                queryset = queryset.filter(**filter_args)

        return queryset
