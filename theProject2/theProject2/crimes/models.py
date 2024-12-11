from django.core.validators import MinValueValidator, MaxValueValidator, MinLengthValidator
from django.db import models
from pkg_resources import require

from theProject2.criminals.models import CriminalMainInfo
from theProject2.crimes.choices import CrimeTypeChoices


class Crime(models.Model):
    name = models.CharField(
        max_length=35,
        validators=[
            MinLengthValidator(2),
        ],
    )
    description = models.TextField(
        blank=False,
        null=False,
    )
    points = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(15)
        ],
    )
    crime_type = models.CharField(
        max_length=3,
        choices=CrimeTypeChoices.choices,
    )
    criminal = models.ForeignKey(
        CriminalMainInfo,
        on_delete=models.CASCADE,
        related_name='crimes',  # Allows access to crimes from a criminal object
        null=True,  # If you want to allow unassigned crimes initially
        blank=True,
    )

    def __str__(self):
        return f"{self.name} ({self.get_crime_type_display()}) - {self.points} points"


