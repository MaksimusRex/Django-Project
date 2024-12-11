from django.db import models

from theProject2.prisons.choices import SecurityLevelChoices


class Prison(models.Model):
    name = models.CharField(max_length=100)
    capacity = models.PositiveIntegerField()
    cells = models.PositiveIntegerField()
    security_level = models.CharField(
        max_length=10,
        choices=SecurityLevelChoices.choices
    )
    picture = models.URLField(
        blank=True,
        null=True,
    )

    @property
    def current_population(self):
        return self.criminals.count()

    def is_full(self):
        return self.current_population >= self.capacity

    def __str__(self):
        return self.name
