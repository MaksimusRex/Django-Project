from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core.validators import MinLengthValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from theProject2.users.managers import AppUserManager
from theProject2.users.validators import UsernameWordCharValidator


class AppUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        unique=True
    )
    username = models.CharField(
        max_length=100,
        validators=[
            MinLengthValidator(4),
            UsernameWordCharValidator(),
        ],
        unique=True,
    )
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )

    objects = AppUserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = 'email'  # TODO: Make a login that works with both username and email. (In the LoginView (the first credential is USERNAME_FIELD which is set in the AuthenticationForm)) # USERNAME_FIELD means the first credential in our auth
    REQUIRED_FIELDS = ["username"]
    def __str__(self):
        return self.email