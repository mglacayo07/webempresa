from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ContactForms


def contact(request):
    kw = { 'contact_form': ContactForms()}
    if request.method == "POST":
        kw['contact_form'] = ContactForms(data=request.POST)
        if kw['contact_form'].is_valid():
            name = request.POST.get('name','')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')
            # Suponemos que salio bien
            return redirect(reverse('contact')+'?ok')  # Eso es como hacer un {% url nombre %} para no tener el url fijo
    return render(request, "contact/contact.html",kw)
