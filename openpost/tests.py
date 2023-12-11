from .models import Column
from django.db.utils import IntegrityError
from django.test import TestCase


class ColumnTests(TestCase):
    def test_create(self):
        o = Column.objects.create(title="aaa", description="bbb")
        self.assertEqual("aaa", str(o))
        self.assertEqual("aaa", o.title)
        self.assertEqual("bbb", o.description)

    def test_title_is_primary_key(self):
        with self.assertRaises(IntegrityError):
            Column.objects.create(title="aaa")
            Column.objects.create(title="aaa")
