from .models import Comment
from .models import Post
from django.db.utils import IntegrityError
from django.test import TestCase

class PostTests(TestCase):
    def setUp(self):
        self.post = Post.objects.create(subject="subject", content="content")

    def test_create(self):
        self.assertEqual("subject", self.post.subject)
        self.assertEqual("subject", str(self.post))
        self.assertEqual("content", self.post.content)

class CommentTests(TestCase):
    def setUp(self):
        self.post = Post.objects.create(subject="subject", content="content")
        self.comment = Comment.objects.create(post=self.post, content="content")

    def test_create(self):
        self.assertEqual("content", str(self.comment))
        self.assertEqual("content", self.comment.content)

    def test_cascade_delete(self):
        self.post.delete()
        self.assertEqual(0, Comment.objects.count())
