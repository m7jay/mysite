from datetime import date
from django.shortcuts import get_object_or_404, render
from .models import Post


def starting_page(request):
    posts = Post.objects.all().order_by("-date_created")[:3]
    return render(request, "blog/index.html", {
        "posts": posts
    })


def all_posts(request):
    return render(request, "blog/all-posts.html", {
        "all_posts": Post.objects.all().order_by("-date_created")
    })


def individual_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, "blog/post-detail.html", {
        "post": post,
        "tags": post.tags.all()
    })
