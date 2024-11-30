from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator
from django.db import models

from theProject2.utils.validators import AgeLimitValidator

UserModel = get_user_model()

class Profile(models.Model):
    user = models.OneToOneField(
        to=UserModel,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    age = models.IntegerField(
        validators=[
            AgeLimitValidator(),
        ],
        blank=True,
        null=True,
    )
    first_name = models.CharField(
        max_length=35,
        validators=[
            MinLengthValidator(2),
        ],
        blank=True,
        null=True,
    )
    last_name = models.CharField(
        max_length=35,
        validators=[
            MinLengthValidator(2),
        ],
        blank=True,
        null=True,
    )
