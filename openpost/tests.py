from .models import Section
from django.db.utils import IntegrityError
from django.test import TestCase


class SectionTests(TestCase):
    def test_create(self):
        o = Section.objects.create(title="aaa", description="bbb")
        self.assertEqual("aaa", str(o))
        self.assertEqual("aaa", o.title)
        self.assertEqual("bbb", o.description)

    def test_title_is_primary_key(self):
        with self.assertRaises(IntegrityError):
            Section.objects.create(title="aaa")
            Section.objects.create(title="aaa")
