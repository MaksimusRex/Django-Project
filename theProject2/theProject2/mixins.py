from django.contrib.auth.mixins import PermissionRequiredMixin
from django.core.exceptions import PermissionDenied


class HasCriminalsChangePermMixin(PermissionRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.has_perm('criminals.can_approve_criminals'):
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


class CanCreateCriminalsMixin(PermissionRequiredMixin):
    permission_required = 'criminals.can_create_criminals'

    def dispatch(self, request, *args, **kwargs):
        # Check if the user has the required permission
        if not request.user.has_perm(self.permission_required):
            raise PermissionDenied("You do not have permission to create criminals.")

        # Proceed with the normal dispatch process
        return super().dispatch(request, *args, **kwargs)