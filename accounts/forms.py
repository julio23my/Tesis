from django.forms import ModelForm
from django.contrib.auth.forms import  UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class SegmentacionForm(forms.ModelForm):
    class Meta:
        model = Segmento
        fields = ['rango', 'mascara', 'direccion', 'subredes', 'reserv']

class SolicitudForm(forms.ModelForm):
    class Meta:
        model = Solicitudes
        fields = ['usuario','solicitud','descripcion','ubicacion']


class ReservaripForm(forms.ModelForm):
    class Meta:
        model = IpReservada
        fields = ['ipv4','ipv6','mac','descripcion','dispositivo']