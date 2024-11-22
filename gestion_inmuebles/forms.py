from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Perfil,Inmueble

class RegistroUsuarioForm(UserCreationForm):
    nombres = forms.CharField(max_length=100)
    apellidos = forms.CharField(max_length=100)
    rut = forms.CharField(max_length=12)
    direccion = forms.CharField(max_length=255)
    telefono = forms.CharField(max_length=15)
    correo_electronico = forms.EmailField()
    tipo_usuario = forms.ChoiceField(choices=Perfil.TIPO_USUARIO)

    class Meta:
        model = User
        fields = [
            'tipo_usuario',
            'nombres',
            'apellidos',
            'rut',
            'direccion',
            'telefono',
            'correo_electronico',
            'username',
            'password1',
            'password2',]

class InmuebleForm(forms.ModelForm):
    class Meta:
        model = Inmueble
        fields = ['nombre',
                'descripcion',
                'metros_construidos',
                'metros_totales',
                'cantidad_estacionamientos',
                'cantidad_habitaciones',
                'cantidad_banos',
                'direccion',
                'comuna',
                'tipo_inmueble',
                'precio_mensual',
                'imagen',
                ]

class EditarPerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = [
            'nombres', 'apellidos', 'rut', 'direccion', 
            'telefono', 'correo_electronico', 'tipo_usuario', 'comuna'
        ]
        widgets = {
            'nombres': forms.TextInput(attrs={'class': 'form-control'}),
            'apellidos': forms.TextInput(attrs={'class': 'form-control'}),
            'rut': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'correo_electronico': forms.EmailInput(attrs={'class': 'form-control'}),
            'tipo_usuario': forms.Select(attrs={'class': 'form-control'}),
            'comuna': forms.Select(attrs={'class': 'form-control'}),
        }