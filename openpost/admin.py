from django.contrib import admin

from .models import Column
from .models import Note
from .models import Comment

admin.site.register(Column)
admin.site.register(Note)
admin.site.register(Comment)
