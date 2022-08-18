from django.shortcuts import render, HttpResponse


def home(request):
    return render(request, "core/home.html")

def about(request):
    return render(request, "core/home.html")

def services(request):
    return render(request, "core/home.html")

def store(request):
    return render(request, "core/home.html")

def contact(request):
    return render(request, "core/home.html")

def blog(request):
    return render(request, "core/home.html")

def sample(request):
    return render(request, "core/home.html")