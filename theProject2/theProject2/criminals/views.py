from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponseForbidden
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, FormView, CreateView, UpdateView, DetailView

from theProject2.criminals.forms import CriminalCreationForm, CriminalDetailInfoForm
from theProject2.criminals.models import CriminalMainInfo, CriminalDetailInfo
from theProject2.mixins import CanCreateCriminalsMixin


class AddCriminalView(CanCreateCriminalsMixin, LoginRequiredMixin, CreateView):
    model = CriminalMainInfo
    form_class = CriminalCreationForm
    template_name = 'criminals/add-criminal.html'
    success_url = reverse_lazy('criminal_dashboard')

    def form_valid(self, form):
        # Assign the currently logged-in user (policeman) to the criminal's record.
        form.instance.policeman = self.request.user
        return super().form_valid(form)


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
            queryset = queryset.order_by('created_at').values()

        elif self.request.user.has_perm('criminals.can_approve_criminals'):
            queryset = queryset.order_by('-is_approved', 'created_at').values() # TODO: Order by is_approved then date added

        if 'query' in self.request.GET:
            query = self.request.GET.get('query')
            queryset = queryset.filter(name__icontains=query)

        return queryset

def approve_criminal(request, pk): # TODO: Make async view
    criminal = CriminalMainInfo.objects.get(pk=pk)
    criminal.is_approved = True
    criminal.save()

    return redirect(request.META.get('HTTP_REFERER'))


class CriminalDetailView(DetailView):
    model = CriminalMainInfo
    template_name = 'criminals/criminal_details.html'
    context_object_name = 'criminal'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['detail_info'] = self.object.detail_info  # Access CriminalDetailInfo via related_name
        except CriminalDetailInfo.DoesNotExist:
            context['detail_info'] = None  # Handle cases where details are missing
        return context


class EditCriminalDetailInfoView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = CriminalDetailInfo
    permission_required = 'criminals.change_criminalmaininfo'
    template_name = 'criminals/edit_criminal_detail_info.html'
    criminal = None
    detail_info = None
    form_class = CriminalCreationForm

    def get_object(self, queryset=None):
        return get_object_or_404(CriminalMainInfo, pk=self.kwargs['pk'])

    def get_success_url(self):
        return reverse('criminal_details', kwargs={'pk': self.object.pk})

    #def get(self, request, *args, **kwargs):
    #    self.criminal = get_object_or_404(CriminalMainInfo, pk=self.kwargs['pk'])
    #    self.detail_info = self.criminal.detail_info if hasattr(self.criminal, 'detail_info') else None
#
    #    if not self.has_permission():
    #        return HttpResponseForbidden("You do not have permission to edit this criminal.")
#
    #    return self.render_to_response(self.get_context_data(
    #        main_form=CriminalCreationForm(instance=self.criminal),
    #        detail_form=CriminalDetailInfoForm(instance=self.detail_info),
    #    ))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        detail_info = getattr(self.object, 'detail_info', None)  # Link detail info if it exists

        context['main_form'] = kwargs.get('main_form', CriminalCreationForm(instance=self.object))
        context['detail_form'] = kwargs.get('detail_form', CriminalDetailInfoForm(instance=detail_info))
        return context

    def post(self, request, *args, **kwargs):
        self.object = get_object_or_404(CriminalMainInfo, pk=self.kwargs['pk'])
        detail_info = getattr(self.object, 'detail_info', None)

        main_form = CriminalCreationForm(request.POST, instance=self.object)
        detail_form = CriminalDetailInfoForm(request.POST, instance=detail_info)

        if main_form.is_valid() and detail_form.is_valid():
            main_form.save()
            detail_instance = detail_form.save(commit=False)
            detail_instance.main_info = self.object
            detail_instance.save()

            return redirect(self.get_success_url())

        return self.render_to_response(self.get_context_data(
            main_form=main_form,
            detail_form=detail_form,
        ))





