from django.db import models


class SecurityLevelChoices(models.TextChoices):
    LOW = 'Low', 'Low Security'
    MID = 'Mid', 'Mid Security'
    HIGH = 'High', 'High Security'