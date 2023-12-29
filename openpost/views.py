from .models import Comment
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

def add_post(request):
    if "section" in request.POST and "subject" in request.POST and "content" in request.POST:
        post = Post.objects.create(section=request.POST["section"],
                                   subject=request.POST["subject"],
                                   content=request.POST["content"])
        post.save()
    return redirect("openpost:index")

def edit_post(request, id):
    if id is not None:
        context = {
            "notices": Post.objects.filter(section="공지사항"),
            "questions": Post.objects.filter(section="질문"),
            "opinions": Post.objects.filter(section="의견"),
            "post": Post.objects.get(id=id),
        }
        return render(request, "openpost/index.html", context=context)
    return redirect("openpost:index")

def update_post(request):
    if "id" in request.POST and "subject" in request.POST and "content" in request.POST:
        Post.objects.filter(id=request.POST["id"]).update(subject=request.POST["subject"],
                                                          content=request.POST["content"])
    return redirect("openpost:index")

def remove_post(request, id):
    if id is not None:
        Post.objects.filter(id=id).delete()
    return redirect("openpost:index")

def add_comment(request):
    if "id" in request.POST and "content" in request.POST:
        post = Post.objects.get(id=request.POST["id"])
        comment = Comment.objects.create(post=post,
                                         content=request.POST["content"])
        comment.save()
    return redirect("openpost:index")

def remove_comment(request, id):
    if id is not None:
        Comment.objects.filter(id=id).delete()
    return redirect("openpost:index")
