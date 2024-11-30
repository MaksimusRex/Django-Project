from django.core.validators import MinLengthValidator
from django.db import models

from theProject2.criminals.models.choices import GenderChoices
from theProject2.utils.validators import AgeLimitValidator


class CriminalMainInfo(models.Model):
    id = models.AutoField(
        primary_key=True
    )
    first_name = models.CharField(
        blank=False,
        null=False,
        max_length=35,
        validators=[
            MinLengthValidator(2),
        ],
    )
    middle_name = models.CharField(
        blank=True,
        null=True,
        max_length=35,
        validators=[
            MinLengthValidator(2),
        ],
    )
    last_name = models.CharField(
        blank=False,
        null=False,
        max_length=35,
        validators=[
            MinLengthValidator(2),
        ],
    )
    gender = models.CharField(
        blank=False,
        null=False,
        max_length=35,
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
    #policeman = models.ForeignKey(AppUser, on_delete=models.CASCADE, limit_choices_to={'role': 'police'}) # TODO: MAKE THE POLICE ROLE AND ALL OTHER ROLES AND THEN MAKE THE ONE TO MANY RELATION IN HERE

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
