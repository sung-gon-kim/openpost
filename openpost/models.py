from django.db import models
from django.utils import timezone

class Column(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    created = timezone.now()

    def __str__(self):
        return self.title

class Note(models.Model):
    column = models.ForeignKey("Column", on_delete=models.CASCADE)
    content = models.TextField()
    created = timezone.now()

    def __str__(self):
        return self.content

class Comment(models.Model):
    note = models.ForeignKey("Note", on_delete=models.CASCADE)
    content = models.TextField()
    created = timezone.now()

    def __str__(self):
        return self.content
