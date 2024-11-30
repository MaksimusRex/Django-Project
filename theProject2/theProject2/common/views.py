from django.shortcuts import render
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = "common/home_page.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['user_name'] = self.request.user.username  # Add username to context
        else:
            context['user_name'] = "Guest"
        return context

#    def get_context_data(self, request):
#        if request.user.is_authenticated:  # Check if a user is logged in
#            current_username = request.user.username  # Retrieve the username
#        else:
#            current_username = "Guest"
#
#        context = {
#            'username': current_username,
#        }
#        return context
#