from .models import Comment
from .models import Post
from django.test import Client
from django.test import TestCase
from django.urls import reverse

class IndexTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_index(self):
        response = self.client.get(reverse("openpost:index"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "openpost/index.html")
        self.assertContains(response, "공지사항")
        self.assertContains(response, "질문")
        self.assertContains(response, "의견")

class PostTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.post = Post.objects.create(section="공지사항", subject="subject", content="content")

    def test_add(self):
        response = self.client.post(reverse("openpost:add_post"), {"section": "공지사항", "subject": "hello", "content": "world"})
        self.assertRedirects(response, reverse("openpost:index"))
        self.assertTrue(Post.objects.filter(subject="hello").exists())

    def test_add_missing_section(self):
        response = self.client.post(reverse("openpost:add_post"), {"subject": "hello", "content": "world"})
        self.assertRedirects(response, reverse("openpost:index"))
        self.assertFalse(Post.objects.filter(subject="hello").exists())

    def test_edit(self):
        response = self.client.get(reverse("openpost:edit_post", kwargs={"id": self.post.id}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "openpost/index.html")
        self.assertContains(response, "subject")
        self.assertContains(response, "content")

    def test_edit_unknown_id(self):
        response = self.client.get(reverse("openpost:edit_post", kwargs={"id": 123}))
        self.assertEqual(response.status_code, 404)

    def test_update(self):
        response = self.client.post(reverse("openpost:update_post"), {"id": self.post.id, "subject": "first", "content": "second"})
        self.assertRedirects(response, reverse("openpost:index"))
        self.assertTrue(Post.objects.filter(subject="first").exists())

    def test_update_missing_id(self):
        response = self.client.post(reverse("openpost:update_post"), {})
        self.assertEqual(response.status_code, 404)

    def test_update_unknown_id(self):
        response = self.client.post(reverse("openpost:update_post"), {"id": 123})
        self.assertEqual(response.status_code, 404)

    def test_remove(self):
        response = self.client.get(reverse("openpost:remove_post", kwargs={"id": self.post.id}))
        self.assertRedirects(response, reverse("openpost:index"))
        self.assertFalse(Post.objects.exists())

    def test_remove_unknown_id(self):
        response = self.client.get(reverse("openpost:remove_post", kwargs={"id": 123}))
        self.assertEqual(response.status_code, 404)
        self.assertTrue(Post.objects.exists())

class CommentTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.post = Post.objects.create(section="공지사항", subject="subject", content="content")
        self.comment = Comment.objects.create(post=self.post, content="comment")

    def test_add(self):
        response = self.client.post(reverse("openpost:add_comment"), {"id": self.post.id, "content": "newComment"})
        self.assertRedirects(response, reverse("openpost:index"))
        self.assertTrue(Comment.objects.filter(content="newComment").exists())

    def test_add_missing_id(self):
        response = self.client.post(reverse("openpost:add_comment"), {"content": "newComment"})
        self.assertRedirects(response, reverse("openpost:index"))
        self.assertFalse(Comment.objects.filter(content="newComment").exists())

    def test_add_unknown_id(self):
        response = self.client.post(reverse("openpost:add_comment"), {"id": 123, "content": "newComment"})
        self.assertRedirects(response, reverse("openpost:index"))
        self.assertFalse(Comment.objects.filter(content="newComment").exists())

    def test_edit(self):
        response = self.client.get(reverse("openpost:edit_comment", kwargs={"id": self.post.id}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "openpost/index.html")
        self.assertContains(response, "comment")

    def test_edit_unknown_id(self):
        response = self.client.get(reverse("openpost:edit_comment", kwargs={"id": 123}))
        self.assertEqual(response.status_code, 404)

    def test_update(self):
        response = self.client.post(reverse("openpost:update_comment"), {"id": self.post.id, "content": "newComment"})
        self.assertRedirects(response, reverse("openpost:index"))
        self.assertTrue(Comment.objects.filter(content="newComment").exists())

    def test_update_missing_id(self):
        response = self.client.post(reverse("openpost:update_comment"), {})
        self.assertEqual(response.status_code, 404)

    def test_update_unknown_id(self):
        response = self.client.post(reverse("openpost:update_comment"), {"id": 123})
        self.assertEqual(response.status_code, 404)

    def test_remove(self):
        response = self.client.get(reverse("openpost:remove_comment", kwargs={"id": self.comment.id}))
        self.assertRedirects(response, reverse("openpost:index"))
        self.assertFalse(Comment.objects.exists())

    def test_remove_parent(self):
        response = self.client.get(reverse("openpost:remove_post", kwargs={"id": self.post.id}))
        self.assertFalse(Comment.objects.exists())

    def test_remove_unknown_id(self):
        response = self.client.get(reverse("openpost:remove_comment", kwargs={"id": 123}))
        self.assertEqual(response.status_code, 404)
        self.assertTrue(Comment.objects.exists())
