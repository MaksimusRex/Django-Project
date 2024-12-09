from django.db import models


class CrimeTypeChoices(models.TextChoices):
    INFRACTION = 'INF', 'Infraction'
    MISDEMEANOR = 'MIS', 'Misdemeanor'
    FELONY_MISDEMEANOR = 'FM', 'Felony-Misdemeanor'
    FELONY = 'FEL', 'Felony'