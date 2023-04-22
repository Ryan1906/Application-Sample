from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate
from Pedidos.models import Clientes


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100, label='Asunto')
    email = forms.EmailField(label='Email')
    message = forms.CharField(widget=forms.Textarea, label='Mensaje')


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Clientes
        fields = ['nombre', 'contraseña', 'email']
        labels = {
            'nombre': 'Nombre',
            'contraseña': 'Contraseña',
            'email': 'Email'
        }
        widgets = {
            'contraseña': forms.PasswordInput()
        }
        error_messages = {
            'nombre': {
                'required': ''
            },
            'contraseña': {
                'required': ''
            }

        }
class LoginForm(forms.Form):
    correo = forms.EmailField(label='Email', max_length=255)
    contrasenia = forms.CharField(label='Contraseña', max_length=255, widget=forms.PasswordInput)

    def clean(self):
        correo = self.cleaned_data.get('correo')
        contrasenia = self.cleaned_data.get('contrasenia')

        if correo and contrasenia:
            return self.cleaned_data

        raise forms.ValidationError('Por favor ingresa tu correo electrónico y contraseña.')
