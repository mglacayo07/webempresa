from django.shortcuts import render
from .forms import ContactForms


def contact(request):
    kw = {
        'contact_form': ContactForms()
    }
    return render(request, "contact/contact.html",kw)
