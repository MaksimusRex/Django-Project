from django.db import models

from theProject2.criminals.models.criminal_main_info import CriminalMainInfo


class CriminalDetailInfo(models.Model):
    main_info = models.OneToOneField(
        CriminalMainInfo,
        on_delete=models.CASCADE,
        related_name='detail_info',
    )
    hair_color = models.CharField(
        max_length=20,
        null=True,
        blank=True,
    )
    eye_color = models.CharField(
        max_length=20,
        null=True,
        blank=True,
    )
    languages = models.CharField(
        max_length=100,
        null=True,
        blank=True,
    )
    race = models.CharField(
        max_length=30,
        null=True,
        blank=True,
    )
    address = models.TextField(
        null=True,
        blank=True,
    )
    date_of_birth = models.DateField(
        null=True,
        blank=True,
    )
    description = models.TextField(
        default='',
        null=True,
        blank=True,
    )


