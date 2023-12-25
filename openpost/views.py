from .models import Post
from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render

def index(request):
    context = {
        "notices": Post.objects.filter(section="공지사항"),
        "questions": Post.objects.filter(section="질문"),
        "opinions": Post.objects.filter(section="의견"),
    }
    return render(request, "openpost/index.html", context=context)

def post(request):
    o = Post.objects.create(section=request.POST["section"],
                            subject=request.POST["subject"],
                            content=request.POST["content"])
    o.save()
    return redirect("openpost:index")
