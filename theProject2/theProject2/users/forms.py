from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator

from theProject2.users.models import Profile
from theProject2.utils.validators import AgeLimitValidator

AppUser = get_user_model()

### AppUser Creation Form ###
class AppUserCreationForm(UserCreationForm):
    class Meta:
        model = AppUser
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'placeholder': 'Enter your username'
        })
        self.fields['email'].widget.attrs.update({
            'placeholder': 'Enter your email address'
        })
        self.fields['password1'].widget.attrs.update({
            'placeholder': 'Create a password'
        })
        self.fields['password2'].widget.attrs.update({
            'placeholder': 'Confirm your password'
        })

    #def clean(self):
    #    username = self.cleaned_data.get('username')
    #    email = self.cleaned_data.get('email')
    #    password1 = self.cleaned_data.get('password1')
    #    password2 = self.cleaned_data.get('password2')
#
    #    if username and password:
    #        # Use authenticate to check credentials
    #        user = authenticate(self.request, username=username, password=password)
    #        if not user:
    #            raise ValidationError(
    #                "The username/email or password is incorrect.",
    #                code='invalid_login'
    #            )
    #    return super().clean()




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

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            # Use authenticate to check credentials
            user = authenticate(self.request, username=username, password=password)
            if not user:
                raise ValidationError(
                    "The username/email or password is incorrect.",
                    code='invalid_login'
                )
        return super().clean()


### 5. Profile Change Form ###
class ChangeUserDetailsForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'age']  # Include the fields you want to display
        widgets = {
            'first_name': forms.TextInput(attrs={
                'placeholder': 'Enter your first name',
                'class': 'form-control',
            }),
            'last_name': forms.TextInput(attrs={
                'placeholder': 'Enter your last name',
                'class': 'form-control',
            }),
            'age': forms.NumberInput(attrs={
                'placeholder': 'Enter your age',
                'class': 'form-control',
            }),
        }

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