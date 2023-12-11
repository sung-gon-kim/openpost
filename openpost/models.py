from django.db import models
from django.utils import timezone


class Section(models.Model):
    title = models.CharField(max_length=128, primary_key=True)
    description = models.CharField(max_length=256)
    created = timezone.now()

    def __str__(self):
        return self.title

