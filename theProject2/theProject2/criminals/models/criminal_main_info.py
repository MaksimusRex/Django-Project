from django.core.validators import MinLengthValidator
from django.db import models

from theProject2.criminals.models.choices import GenderChoices
from theProject2.users.models import AppUser
from theProject2.utils.validators import AgeLimitValidator


class CriminalMainInfo(models.Model):
    NAME_MAX_LENGTH = 35
    id = models.AutoField(
        primary_key=True
    )
    first_name = models.CharField(
        blank=False,
        null=False,
        max_length=NAME_MAX_LENGTH,
        validators=[
            MinLengthValidator(2),
        ],
    )
    middle_name = models.CharField(
        blank=True,
        null=True,
        max_length=NAME_MAX_LENGTH,
        validators=[
            MinLengthValidator(2),
        ],
    )
    last_name = models.CharField(
        blank=False,
        null=False,
        max_length=NAME_MAX_LENGTH,
        validators=[
            MinLengthValidator(2),
        ],
    )
    gender = models.CharField(
        blank=False,
        null=False,
        choices=GenderChoices.choices,
    )
    height = models.DecimalField(
        max_digits=5,
        decimal_places=2
    )  # Height in cm
    age = models.PositiveIntegerField(
        validators=[
            AgeLimitValidator(),
        ]
    )
    picture = models.URLField(
        blank=True,
        null=True,
    )
    is_approved = models.BooleanField(
        default=False,
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    policeman = models.ForeignKey(
        AppUser,
        on_delete=models.CASCADE,
        limit_choices_to={'role': 'Police Officer'},
        null=True,
        default=None,
    )

    class Meta:
        permissions = [
            ('can_approve_criminals', 'Can approve criminals'),
        ]

    def __str__(self):
        return f"{self.first_name} {self.middle_name} {self.last_name}"
