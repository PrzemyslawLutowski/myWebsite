# from django.http import Http404
# from django.shortcuts import render
# from .models import BlogPost
#
#
# def post_list(request):
#     posts = BlogPost.objects.all()
#     return render(
#         request,
#         "blog/post/list.html",
#         {'posts': posts})
#
#
# def post_detail(request, id):
#     try:
#         post = BlogPost.objects.get(id=id)
#     except BlogPost.DoesNotExist:
#         raise Http404("Post does not exist")
#
#     return render(request, "blog/post/list.html",
#                   {'post': post})
