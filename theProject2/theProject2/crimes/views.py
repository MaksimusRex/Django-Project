from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render, redirect

from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.urls import reverse
from django.views import View
from django.views.generic import DetailView, UpdateView, DeleteView

from .models import Crime, CriminalMainInfo
from theProject2.crimes.forms import CrimeForm


def add_crime(request, criminal_id):
    criminal = get_object_or_404(CriminalMainInfo, pk=criminal_id)

    if request.method == 'POST':
        form = CrimeForm(request.POST)
        if form.is_valid():
            crime = form.save(commit=False)
            crime.criminal = criminal
            crime.save()
            return JsonResponse({'success': True})

    else:
        form = CrimeForm()

    return render(request, 'crimes/crime_form.html', {'form': form, 'criminal': criminal})


class DetailCrimeView(DetailView):
    model = Crime
    template_name = 'crimes/details.html'
    context_object_name = 'crime'

    def get_object(self):
        return get_object_or_404(Crime, pk=self.kwargs['pk'])


class EditCrimeView(UpdateView):
    model = Crime
    form_class = CrimeForm
    template_name = 'crimes/edit_crime.html'
    permission_required = 'crimes.change_crime'  # Ensure this permission exists
    fields = ['name', 'description', 'date', 'points']
    context_object_name = 'crime'

    def get_object(self, queryset=None):
        # Retrieve the vehicle based on its primary key (from URL)
        return get_object_or_404(Crime, pk=self.kwargs['pk'])

    def get_success_url(self):
        # Redirect back to the vehicle's detail page after editing the vehicle
        return reverse('detail_crime', kwargs={'pk': self.object.pk})


class DeleteCrimeView(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = 'crimes.delete_crime'

    def post(self, request, pk):
        crime = get_object_or_404(Crime, pk=pk)
        criminal_id = crime.criminal.id  # Store the associated criminal ID
        crime.delete()
        return redirect(reverse('criminal_details', kwargs={'pk': criminal_id}))