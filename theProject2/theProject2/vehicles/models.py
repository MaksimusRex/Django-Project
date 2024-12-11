from django.core.validators import MaxValueValidator
from django.db import models
from theProject2.criminals.models import CriminalMainInfo
from datetime import date

class Vehicle(models.Model):
    VEHICLE_TYPES = [
        ('Car', 'Car'),
        ('Motorcycle', 'Motorcycle'),
        ('Truck', 'Truck'),
        ('Van', 'Van'),
        ('Other', 'Other'),
    ]

    criminal = models.ForeignKey(
        CriminalMainInfo,
        on_delete=models.CASCADE,
        related_name='vehicles'
    )
    vehicle_type = models.CharField(
        max_length=20,
        choices=VEHICLE_TYPES,
        default='Other'
    )
    make = models.CharField(max_length=50)  # e.g., Toyota, Ford
    model = models.CharField(max_length=50)  # e.g., Corolla, Mustang
    year = models.PositiveIntegerField(
        validators=[MaxValueValidator(limit_value=date.today().year)],
    )  # Year of manufacture
    license_plate = models.CharField(max_length=15, unique=True)  # License plate number
    color = models.CharField(max_length=30, blank=True, null=True)  # Optional field for color

    def __str__(self):
        return f"{self.make} {self.model} ({self.year}) - {self.license_plate}"