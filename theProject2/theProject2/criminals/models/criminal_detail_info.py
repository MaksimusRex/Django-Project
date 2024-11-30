from django.db import models

from theProject2.criminals.models.criminal_main_info import CriminalMainInfo


class CriminalDetailInfo(models.Model):
    main_info = models.OneToOneField(
        CriminalMainInfo,
        on_delete=models.CASCADE,
        related_name='detail_info',
    )
    hair_color = models.CharField(
        max_length=20
    )
    eye_color = models.CharField(
        max_length=20
    )
    languages = models.CharField(
        max_length=100
    )
    race = models.CharField(
        max_length=30
    )
    address = models.TextField()
    date_of_birth = models.DateField()


