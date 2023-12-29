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
        self.client.post(reverse("openpost:add_post"), {"section": "공지사항", "subject": "subject", "content": "content"})

    def test_add(self):
        response = self.client.post(reverse("openpost:add_post"), {"section": "공지사항", "subject": "hello", "content": "world"})
        self.assertRedirects(response, reverse("openpost:index"))
        self.assertEqual(Post.objects.filter(subject="hello").count(), 1)

    def test_add_missing_param(self):
        response = self.client.post(reverse("openpost:add_post"), {"subject": "hello", "content": "world"})
        self.assertRedirects(response, reverse("openpost:index"))
        self.assertEqual(Post.objects.filter(subject="hello").count(), 0)

    def test_edit(self):
        response = self.client.get(reverse("openpost:edit_post", kwargs={"id": 1}))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "openpost/index.html")
        self.assertContains(response, "subject")
        self.assertContains(response, "content")

    def test_edit_unknown_id(self):
        response = self.client.get(reverse("openpost:edit_post", kwargs={"id": 123}))
        self.assertEquals(response.status_code, 404)

    def test_update(self):
        response = self.client.post(reverse("openpost:update_post"), {"id": 1, "subject": "first", "content": "second"})
        self.assertRedirects(response, reverse("openpost:index"))
        self.assertEqual(Post.objects.filter(subject="first").count(), 1)

    def test_update_missing_id(self):
        response = self.client.post(reverse("openpost:update_post"), {})
        self.assertEqual(response.status_code, 404)

    def test_update_unknown_id(self):
        response = self.client.post(reverse("openpost:update_post"), {"id": 123})
        self.assertEqual(response.status_code, 404)

    def test_remove(self):
        response = self.client.get(reverse("openpost:remove_post", kwargs={"id": 1}))
        self.assertRedirects(response, reverse("openpost:index"))
        self.assertEqual(Post.objects.count(), 0)

    def test_remove_unknown_id(self):
        response = self.client.get(reverse("openpost:remove_post", kwargs={"id": 123}))
        self.assertEqual(response.status_code, 404)
        self.assertEqual(Post.objects.count(), 1)
