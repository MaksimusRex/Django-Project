from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.contrib.messages import success
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DetailView

from theProject2.prisons.forms import PrisonCreationForm, PrisonSearchForm
from theProject2.prisons.models import Prison


class PrisonListView(ListView):
    model = Prison
    template_name = 'prisons/prison_dashboard.html'
    context_object_name = 'prisons'
    paginate_by = 4

    def get_queryset(self):
        queryset = self.model.objects.all()

        name = self.request.GET.get('name')  # Get the name from the query parameters

        if name:
            queryset = queryset.filter(
                name__icontains=name
            )  # Filter by first or last name (case-insensitive)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = PrisonSearchForm(self.request.GET)
        return context


class PrisonCreateView(PermissionRequiredMixin, CreateView):
    model = Prison
    form_class = PrisonCreationForm
    template_name = 'prisons/create_prison.html'
    success_url = reverse_lazy('prisons_dashboard')

    permission_required = 'prisons.add_prison'

    raise_exception = True  # Raise a 403 Forbidden error if the user lacks permission
    permission_denied_message = "You do not have permission to add a prison."

class EditPrisonView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Prison
    form_class = PrisonCreationForm
    template_name = 'prisons/edit_prison.html'
    permission_required = 'prisons.change_prison'

    def get_object(self, queryset=None):
        # Retrieve the vehicle based on its primary key (from URL)
        return get_object_or_404(Prison, pk=self.kwargs['pk'])

    def get_success_url(self):
        # Redirect back to the vehicle's detail page after editing the vehicle
        return reverse('detail_prison', kwargs={'pk': self.object.pk})



class DetailPrisonView(DetailView):
    model = Prison
    template_name = 'prisons/details.html'
    context_object_name = 'prison'

    def get_object(self):
        return get_object_or_404(Prison, pk=self.kwargs['pk'])



class DeletePrisonView(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = 'prisons.delete_prison'

    def post(self, request, pk):
        prison = get_object_or_404(Prison, pk=pk)
        prison.delete()
        return redirect(reverse('prisons_dashboard'))
