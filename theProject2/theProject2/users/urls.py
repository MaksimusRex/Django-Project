from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from theProject2.users.forms import EmailOrUsernameLoginForm
from theProject2.users.views import UserRegisterView, UserDetailView, PoliceOfficerRegisterView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('register-police-officer/', PoliceOfficerRegisterView.as_view(), name='police_officer_register'),
    path('login/', LoginView.as_view(authentication_form=EmailOrUsernameLoginForm), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile-details/', UserDetailView.as_view(), name='user_details'),
]