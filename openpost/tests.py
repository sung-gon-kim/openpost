from .models import Column
from .models import Note
from django.db.utils import IntegrityError
from django.test import TestCase


class ColumnTests(TestCase):
    def setUp(self):
        self.column = Column.objects.create(title="column", description="description")

    def test_create(self):
        self.assertEqual("column", str(self.column))
        self.assertEqual("column", self.column.title)
        self.assertEqual("description", self.column.description)

    def test_title_is_primary_key(self):
        with self.assertRaises(IntegrityError):
            Column.objects.create(title="column", description="description")

class NoteTests(TestCase):
    def setUp(self):
        self.column = Column.objects.create(title="column", description="description")
        self.note = Note.objects.create(column=self.column, title="note", content="content")

    def test_create(self):
        self.assertEqual("note", str(self.note))
        self.assertEqual("note", self.note.title)
        self.assertEqual("content", self.note.content)

    def test_uid_is_primary_key(self):
        with self.assertRaises(IntegrityError):
            Note.objects.create(column=self.column, id=1, title="note", content="content")

    def test_title_is_not_unique(self):
        Note.objects.create(column=self.column, title="note", content="content")

    def test_cascade_delete(self):
        self.column.delete()
        self.assertEqual(0, Note.objects.count())
