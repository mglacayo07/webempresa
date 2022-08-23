from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForms


def contact(request):
    kw = { 'contact_form': ContactForms()}
    if request.method == "POST":
        kw['contact_form'] = ContactForms(data=request.POST)
        if kw['contact_form'].is_valid():
            name = request.POST.get('name','')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')
            # Enviamos el correo y redireccionamos
            email = EmailMessage(
                "La Caffetiera: Nuevo mensaje de contaco",  # asunto
                "De {} <{}>\n\nEscribió:\n\n{}".format(name,email,content),  # cuerpo
                "no-contestar@inbox.mailtrap.io",  # email_origen
                ["maria@madd.com.mx"],  # email_destino
                reply_to=[email]  # email en caso de respuesta
            )
            try:
                email.send()
                # Ha ido buen, redireccionamos a OK
                return redirect(reverse('contact') + '?ok')
            except:
                # Algo no ha ido bien, redireccionamos a FAIL
                return redirect(reverse('contact') + '?fail')

    return render(request, "contact/contact.html",kw)
