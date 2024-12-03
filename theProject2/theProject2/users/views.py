from django.contrib.auth import login, get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import Group
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView

from theProject2.users.forms import AppUserCreationForm, ChangeUserDetailsForm, PoliceOfficerCreationForm

UserModel = get_user_model()

class UserRegisterView(CreateView):
    form_class = AppUserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()  # Save the new user
        login(self.request, user, backend='theProject2.users.authentication.EmailOrUsernameAuthentication')  # Log the user in
        return super().form_valid(form)

class ChangeProfileDetails:
    form_class = ChangeUserDetailsForm
    template_name = 'registration/change_profile_details.html'
    success_url = reverse_lazy(template_name)

class UserDetailView(LoginRequiredMixin, DetailView):
    model = UserModel
    template_name = 'user_details/profile_page.html'  # Path to template
    context_object_name = 'user_detail'  # Name of the context variable in the template

    def get_object(self, queryset=None):
        # Display the details of the logged-in user
        return self.request.user


# Limit the number of form submissions to 1 per day to protect against spam of requests
#@method_decorator(ratelimit(key='ip', rate='1/d', method='POST'), name='form_valid') TODO: Maybe finish
class PoliceOfficerRegisterView(CreateView):
    form_class = PoliceOfficerCreationForm
    template_name = 'registration/police_officer_register.html'
    success_url = reverse_lazy('login')

    # Automatically adds the Police officer role to the registered user if the form is successful
    def form_valid(self, form):
        response = super().form_valid(form)
        user = self.object
        police_officer_group = Group.objects.get(name='Police Officer')
        user.groups.add(police_officer_group)

        return response
