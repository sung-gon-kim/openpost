from .models import Column
from .models import Comment
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

    def test_title_is_not_unique(self):
        Column.objects.create(title="column", description="description")

class NoteTests(TestCase):
    def setUp(self):
        self.column = Column.objects.create(title="column", description="description")
        self.note = Note.objects.create(column=self.column, content="content")

    def test_create(self):
        self.assertEqual("content", str(self.note))
        self.assertEqual("content", self.note.content)

    def test_content_is_not_unique(self):
        Note.objects.create(column=self.column, content="content")

    def test_cascade_delete(self):
        self.column.delete()
        self.assertEqual(0, Note.objects.count())

class CommentTests(TestCase):
    def setUp(self):
        self.column = Column.objects.create(title="column", description="description")
        self.note = Note.objects.create(column=self.column, content="content")
        self.comment = Comment.objects.create(note=self.note, content="content")

    def test_create(self):
        self.assertEqual("content", str(self.comment))
        self.assertEqual("content", self.comment.content)

    def test_content_is_not_unique(self):
        Comment.objects.create(note=self.note, content="content")

    def test_cascade_delete(self):
        self.note.delete()
        self.assertEqual(0, Comment.objects.count())
