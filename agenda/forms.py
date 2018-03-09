from django import forms
from agenda.models import Contacto, Telefono, Social

class ContactoForm(forms.ModelForm):
    
    class Meta:
        model = Contacto
        fields = [
            'nombre',
            'apellidos',
            'correo',
            'organizacion',
        ]

class TelefonoForm(forms.ModelForm):
    
    class Meta:
        model = Telefono
        fields = [
            'tipo',
            'numero',
        ]        

class SocialForm(forms.ModelForm):
    
    class Meta:
        model = Social
        fields = [
            'red',
            'urln',
        ]        