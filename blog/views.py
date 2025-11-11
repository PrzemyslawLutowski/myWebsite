from django.shortcuts import render
from .models import BlogPost


def post_list(request):
    posts = BlogPost.objects.all()
    return render(
        request,
        "blog/post/list.html",
        {'posts': posts},
    )
