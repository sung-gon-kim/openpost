from django.db import models
from django.utils import timezone

SHORT_CHAR_LENGTH = 128

class Column(models.Model):
    title = models.CharField(max_length=SHORT_CHAR_LENGTH)
    description = models.TextField()
    created = timezone.now()

    def __str__(self):
        return self.title

class Note(models.Model):
    column = models.ForeignKey("Column", on_delete=models.CASCADE)
    title = models.CharField(max_length=SHORT_CHAR_LENGTH)
    content = models.TextField()
    created = timezone.now()

    def __str__(self):
        return self.title

class Comment(models.Model):
    note = models.ForeignKey("Note", on_delete=models.CASCADE)
    content = models.TextField()
    created = timezone.now()

    def __str__(self):
        return self.content
