from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import UpdateView, DetailView, ListView

from theProject2.criminals.models import CriminalMainInfo
from theProject2.vehicles.forms import VehicleForm, VehicleSearchForm
from theProject2.vehicles.models import Vehicle


class AddVehicleView(View):
    template_name = 'vehicles/vehicle_form.html'

    def get(self, request, criminal_id):
        """Render the empty vehicle form for the modal."""
        criminal = get_object_or_404(CriminalMainInfo, pk=criminal_id)
        vehicle_form = VehicleForm()
        return render(request, self.template_name, {
            'vehicle_form': vehicle_form,
            'criminal': criminal,
        })

    def post(self, request, criminal_id):
        """Handle the form submission."""
        criminal = get_object_or_404(CriminalMainInfo, pk=criminal_id)
        vehicle_form = VehicleForm(request.POST)

        if vehicle_form.is_valid():
            vehicle = vehicle_form.save(commit=False)
            vehicle.criminal = criminal
            vehicle.save()
            return JsonResponse({
                'success': True,
                'vehicle_id': vehicle.id,
                'make': vehicle.make,
                'model': vehicle.model,
                'year': vehicle.year,
            })

        return JsonResponse({
            'success': False,
            'form_html': render(request, self.template_name, {'vehicle_form': vehicle_form}).content.decode(),
        })


class EditVehicleView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Vehicle
    form_class = VehicleForm
    template_name = 'vehicles/edit_vehicle.html'
    permission_required = 'vehicles.change_vehicle'  # Ensure this permission exists

    def get_object(self, queryset=None):
        # Retrieve the vehicle based on its primary key (from URL)
        return get_object_or_404(Vehicle, pk=self.kwargs['pk'])

    def get_success_url(self):
        # Redirect back to the vehicle's detail page after editing the vehicle
        return reverse('detail_vehicle', kwargs={'pk': self.object.pk})


class DeleteVehicleView(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = 'vehicles.delete_vehicle'

    def post(self, request, pk):
        vehicle = get_object_or_404(Vehicle, pk=pk)
        criminal_id = vehicle.criminal.id  # Store the associated criminal ID
        vehicle.delete()
        return redirect(reverse('criminal_details', kwargs={'pk': criminal_id}))


class DetailVehicleView(DetailView):
    model = Vehicle
    template_name = 'vehicles/details.html'
    context_object_name = 'vehicle'

    def get_object(self):
        return get_object_or_404(Vehicle, pk=self.kwargs['pk'])



class DashboardVehicleView(ListView):
    template_name = 'vehicles/vehicle_dashboard.html'
    context_object_name = 'vehicles'
    model = Vehicle
    paginate_by = 4

    def get_queryset(self):
        queryset = self.model.objects.all()
        search_params = self.request.GET

        vehicle_type_filter = search_params.get('vehicle_type')
        model_filter = search_params.get('model')
        year_filter = search_params.get('year')
        color_filter = search_params.get('color')

        if vehicle_type_filter:
            queryset = queryset.filter(vehicle_type=vehicle_type_filter)
        if model_filter:
            queryset = queryset.filter(model__icontains=model_filter)
        if year_filter:
            queryset = queryset.filter(year=year_filter)
        if color_filter:
            queryset = queryset.filter(color__icontains=color_filter)

        return queryset.order_by('year')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = VehicleSearchForm(self.request.GET)  # Pre-fill with current filters
        return context