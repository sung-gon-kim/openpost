from django.db import models
from django.utils import timezone


class Column(models.Model):
    title = models.CharField(max_length=128, primary_key=True)
    description = models.CharField(max_length=256)
    created = timezone.now()

    def __str__(self):
        return self.title

class Note(models.Model):
    column = models.ForeignKey("Column", on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    content = models.TextField()
    created = timezone.now()

    def __str__(self):
        return self.title
