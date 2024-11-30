from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from django import forms
from django.core.validators import MinLengthValidator

from theProject2.users.models import Profile
from theProject2.utils.validators import AgeLimitValidator

AppUser = get_user_model()

### AppUser Creation Form ###
class AppUserCreationForm(UserCreationForm):
    class Meta:
        model = AppUser
        fields = ('username', 'email')


### Police Officer Creation Form ###
class PoliceOfficerCreationForm(AppUserCreationForm):
    first_name = forms.CharField(
        max_length=35,
        validators=[
            MinLengthValidator(2),
        ],
        required=True
    )
    last_name = forms.CharField(
        max_length=35,
        validators=[
            MinLengthValidator(2),
        ],
        required=True
    )
    age = forms.IntegerField(
        validators=[
            AgeLimitValidator(),
        ],
        required=True
    )

    class Meta(AppUserCreationForm.Meta):
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_active = False  # Set account as inactive until approval

        if commit:
            user.set_password(self.cleaned_data['password1'])  # Hash password securely
            user.save()

            Profile.objects.create(
                user=user,
                first_name=self.cleaned_data['first_name'],
                last_name=self.cleaned_data['last_name'],
                age=self.cleaned_data['age']
            )
        return user


### AppUser Change Form ###
class AppUserChangeForm(UserChangeForm):
    class Meta:
        model = AppUser
        fields = "__all__"


### Email or Username Login Form ###
class EmailOrUsernameLoginForm(AuthenticationForm):
    username = forms.CharField(label="Username or Email", max_length=254)


### 5. Profile Change Form ###
class ChangeUserDetailsForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']  # Prevent user field from being changed by form users


#
#class AppUserCreationForm(UserCreationForm):
#    class Meta(UserCreationForm.Meta):
#        model = get_user_model()
#        fields = ('username', 'email')
#
#
#class PoliceOfficerCreationForm(AppUserCreationForm):
#    first_name = forms.CharField(max_length=40, required=True)
#    last_name = forms.CharField(max_length=40, required=True)
#    age = forms.IntegerField(required=False)
#
#    class Meta:
#        model = get_user_model()
#        fields = ['username', 'email', 'password']
#
#    def save(self, commit=True):
#        user = super().save(commit=False)
#        user.is_active = False  # Set account as inactive until approval
#        if commit:
#            user.set_password(self.cleaned_data['password'])  # Hash password
#            user.save()
#
#            # Save the profile
#            Profile.objects.create(
#                user=user,
#                first_name=self.cleaned_data['first_name'],
#                last_name=self.cleaned_data['last_name'],
#                age=self.cleaned_data.get('age')
#            )
#        return user
#
#
#
#
#class AppUserChangeForm(UserChangeForm):
#    class Meta(UserChangeForm.Meta):
#        model = get_user_model()
#        fields = "__all__"
#
#class EmailOrUsernameLoginForm(AuthenticationForm):
#    username = forms.CharField(label="Username or Email", max_length=254)
#
#class ChangeUserDetailsForm(forms.ModelForm):
#    class Meta:
#        model = Profile
#        fields = "__all__"
#