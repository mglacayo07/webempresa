from django.shortcuts import render
from .models import Post


def blog(request):
    kw = {'posts': Post.objects.all()}
    return render(request, "blog/blog.html",kw)