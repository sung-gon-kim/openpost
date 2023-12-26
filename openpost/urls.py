from django.urls import path

from . import views

app_name = "openpost"
urlpatterns = [
    path("", views.index, name="index"),
    path("post/add", views.add_post, name="add_post"),
    path("post/remove/<int:id>", views.remove_post, name="remove_post"),
]
