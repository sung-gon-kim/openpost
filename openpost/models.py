from django.db import models
from django.utils import timezone
from django.utils.translation import gettext as _
from model_utils import Choices

class Post(models.Model):
    SECTION = Choices('공지사항', '질문', '의견')
    section = models.CharField(choices=SECTION, default=SECTION.공지사항, max_length=10)
    content = models.TextField()
    created = timezone.now()

    def __str__(self):
        return self.content

class Comment(models.Model):
    post = models.ForeignKey("Post", on_delete=models.CASCADE)
    content = models.TextField()
    created = timezone.now()

    def __str__(self):
        return self.content
