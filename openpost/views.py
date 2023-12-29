from .models import Comment
from .models import Post
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
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
    context = {
        "notices": Post.objects.filter(section="공지사항"),
        "questions": Post.objects.filter(section="질문"),
        "opinions": Post.objects.filter(section="의견"),
        "post": get_object_or_404(Post, id=id),
    }
    return render(request, "openpost/index.html", context=context)

def update_post(request):
    post = get_object_or_404(Post, id=request.POST.get("id", 0))
    post.subject = request.POST.get("subject", "")
    post.content = request.POST.get("content", "")
    post.save()
    return redirect("openpost:index")

def remove_post(request, id):
    post = get_object_or_404(Post, id=id)
    post.delete()
    return redirect("openpost:index")

def add_comment(request):
    if "id" in request.POST and Post.objects.filter(id=request.POST["id"]).exists() and "content" in request.POST:
        post = Post.objects.get(id=request.POST["id"])
        comment = Comment.objects.create(post=post,
                                         content=request.POST["content"])
        comment.save()
    return redirect("openpost:index")

def edit_comment(request, id):
    context = {
        "notices": Post.objects.filter(section="공지사항"),
        "questions": Post.objects.filter(section="질문"),
        "opinions": Post.objects.filter(section="의견"),
        "comment": get_object_or_404(Comment, id=id),
    }
    return render(request, "openpost/index.html", context=context)

def update_comment(request):
    comment = get_object_or_404(Comment, id=request.POST.get("id", 0))
    comment.content = request.POST.get("content", "")
    comment.save()
    return redirect("openpost:index")

def remove_comment(request, id):
    comment = get_object_or_404(Comment, id=id)
    comment.delete()
    return redirect("openpost:index")
