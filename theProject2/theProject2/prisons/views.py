from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from theProject2.prisons.forms import PrisonCreationForm
from theProject2.prisons.models import Prison


class PrisonListView(ListView):
    model = Prison
    template_name = 'prisons/prison_list.html'
    context_object_name = 'prisons'


class PrisonCreateView(PermissionRequiredMixin, CreateView):
    model = Prison
    form_class = PrisonCreationForm
    template_name = 'prisons/create_prison.html'
    success_url = reverse_lazy('prison_list')

    # Specify the required permission
    permission_required = 'prisons.add_prison'

    # Customize the behavior when the user lacks permission
    raise_exception = True  # Raise a 403 Forbidden error if the user lacks permission
    permission_denied_message = "You do not have permission to add a prison."
