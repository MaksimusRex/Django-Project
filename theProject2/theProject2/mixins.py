from django.contrib.auth.mixins import AccessMixin


class HasCriminalsChangePermMixin(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.has_perm('criminals.can_approve_criminals'):
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)