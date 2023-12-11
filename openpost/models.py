from django.db import models
from django.utils import timezone


SHORT_CHAR_LENGTH = 128
LONG_CHAR_LENGTH = 512

class Column(models.Model):
    title = models.CharField(max_length=SHORT_CHAR_LENGTH)
    description = models.CharField(max_length=LONG_CHAR_LENGTH)
    created = timezone.now()

    def __str__(self):
        return self.title

class Note(models.Model):
    column = models.ForeignKey("Column", on_delete=models.CASCADE)
    title = models.CharField(max_length=SHORT_CHAR_LENGTH)
    content = models.CharField(max_length=LONG_CHAR_LENGTH)
    created = timezone.now()

    def __str__(self):
        return self.title

class Comment(models.Model):
    note = models.ForeignKey("Note", on_delete=models.CASCADE)
    content = models.CharField(max_length=LONG_CHAR_LENGTH)
    created = timezone.now()

    def __str__(self):
        return self.content
