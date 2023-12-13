from .models import Column
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context = { "columns": Column.objects.all() }
    return render(request, "openpost/index.html", context=context)
