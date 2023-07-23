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
                return True
        if not permitted:
            self.permission_denied(
                request,
                message='Permission denied. Ask the manager team for more details.',
            )

    def check_object_permissions(self, request, obj):
        permitted = False
        for permission in self.get_permissions():
            if permission.has_object_permission(request, self, obj):
                return
        if not permitted:
            self.permission_denied(
                request,
                message='Permission denied. Ask the manager team for more details.',
            )
