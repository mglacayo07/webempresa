from django.shortcuts import render, get_object_or_404
from .models import Post, Category


def blog(request):
    kw = {'posts': Post.objects.all()}
    return render(request, "blog/blog.html",kw)


def category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    kw = {
        'category': category,
        ##'posts': Post.objects.filter(categories=category)
    }
    return render(request,"blog/category.html", kw)
