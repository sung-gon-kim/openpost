from django.urls import path

from . import views

app_name = "openpost"
urlpatterns = [
    path("", views.index, name="index"),
    path("post/add", views.add_post, name="add_post"),
    path("post/edit/<int:id>", views.edit_post, name="edit_post"),
    path("post/update", views.update_post, name="update_post"),
    path("post/remove/<int:id>", views.remove_post, name="remove_post"),
    path("comment/add", views.add_comment, name="add_comment"),
    path("comment/edit/<int:id>", views.edit_comment, name="edit_comment"),
    path("comment/update", views.update_comment, name="update_comment"),
    path("comment/remove/<int:id>", views.remove_comment, name="remove_comment"),
]
