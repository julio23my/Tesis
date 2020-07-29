from django.forms import ModelForm
from django.contrib.auth.forms import  UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *
from django.forms import inlineformset_factory

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class SegmentacionForm(forms.ModelForm):

    class Meta:
        model = Segmento
        fields = ['rango', 'mascara']

class SegmentacionForm2(forms.ModelForm):
    class Meta:
        model = Segmento
        fields = ['rango', 'mascara']

class SolicitudForm(forms.ModelForm):
    class Meta:
        model = Solicitudes
        fields = ['usuario','solicitud','descripcion','ubicacion',]



class ReservaripForm(forms.ModelForm):
    class Meta:
        model = IpReservada
        fields = ['ipv4','ipv6','mac','descripcion','dispositivo']

class DeviceForm(forms.ModelForm):
    class Meta:
        model = Device
        fields = ['dvt','ipv4','ipv6','ssh','telnet','conf','conf_t','name','ubicacion','modelo','serial','marca','responsable']
class PuertoForm(forms.ModelForm):
    class Meta:
        model = Puerto
        exclude = ()

PuertoFormSet = inlineformset_factory(Device, Puerto, form=PuertoForm, extra=1)

class IpReservadaForm(forms.ModelForm):
    class Meta:
        model = IpReservada
        fields = ['ipv4', 'ipv6', 'mac', 'descripcion','dispositivo']


class SendConfForm(forms.ModelForm):
    devices = forms.ModelMultipleChoiceField(queryset= Device.objects.filter(dvt='R') | Device.objects.filter(dvt='S'), widget=forms.CheckboxSelectMultiple(), required=False)
    class Meta:
        model = SendConf
        fields = ['devices','conf']

class UbicacionForm(forms.ModelForm):
    class Meta:
        model = Ubicacion
        fields = ['localidad','departamento']


class UbicacionForm(forms.ModelForm):
    class Meta:
        model = Ubicacion
        fields = ['localidad','departamento']