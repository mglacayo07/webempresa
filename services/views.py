from django.shortcuts import render
from .models import Service

def services(request):
    kw = {'services':Service.objects.all()}
    return render(request, "services/services.html", kw)
