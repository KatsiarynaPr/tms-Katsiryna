from django.http import HttpRequest
from django.http import HttpResponse
from django.shortcuts import render, redirect

from application.blog.models import Post


def all_posts_view(request) -> HttpResponse:
    contex = {
        "object_list": Post.objects.all(),
    }
    result = render(request, "blog/blog.html", context=contex)

    return HttpResponse(result)

def new_post_view(request: HttpRequest):
    title = request.POST["title"]
    content = request.POST["content"]
    post = Post(
        title=title,
        content=content,
    )
    post.save()
    return redirect("/b/")

def reset_post_view(request: HttpRequest):
    Post.objects.all().delete()
    return redirect("/b/")

