from django.urls import path

from . import views

app_name = "openpost"
urlpatterns = [
    path("", views.index, name="index"),
    path("post/", views.post, name="post"),
]
