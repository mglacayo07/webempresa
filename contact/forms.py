from django import forms


class ContactForms(forms.Form):
    name = forms.CharField(label="Nombre", required=True)
    email = forms.EmailField(label="Correo electrónico", required=True)
    content = forms.CharField(label="Contenido", required=True, widget=forms.Textarea)
