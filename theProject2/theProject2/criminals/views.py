from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, FormView, CreateView

from theProject2.criminals.forms import CriminalCreationForm
from theProject2.criminals.models import CriminalMainInfo


class AddCriminalView(LoginRequiredMixin, CreateView):
    model = CriminalMainInfo
    form_class = CriminalCreationForm
    template_name = 'criminals/add-criminal.html'
    success_url = reverse_lazy('criminal-dashboard')

class CriminalDashboardView(ListView):
    template_name = 'criminals/criminal_dashboard.html'
    context_object_name = 'criminals'
    # form_class =  TODO: SEARCH FORM (add FormView)
    paginate_by = 4 # Number of objects per page
    success_url = reverse_lazy('criminal_dashboard')
    model = CriminalMainInfo

    def get_queryset(self):
        queryset = self.model.objects.all()

        if not self.request.user.has_perm('criminals.can_approve_criminals'):
            queryset = queryset.filter(is_approved=True)

        if 'query' in self.request.GET:
            query = self.request.GET.get('query')
            queryset = queryset.filter(name__icontains=query)


        return queryset

def approve_criminal(request, pk): # TODO: Make async view
    criminal = CriminalMainInfo.objects.get(pk=pk)
    criminal.is_approved = True
    criminal.save()



