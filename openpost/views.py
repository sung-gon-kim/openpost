from .models import Post
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context = { "data": Post.objects.all() }
    return render(request, "openpost/index.html", context=context)
