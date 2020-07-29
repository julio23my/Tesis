from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from .forms import *
from .decorators import unauthenticated_user
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import *
# import netmiko
# import napalm
import sys
from time import sleep
import paramiko

# Create your views here.
def home_view(request):
    context = {}
    return render(request, 'accounts/home/home.html', context)


@unauthenticated_user
def LoginPage(request):
    if request.method =='POST':
        usernames = request.POST['username']
        passwords = request.POST['password']
        user = authenticate(request, username=usernames, password=passwords)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect('Dashboard')
        else:
            messages.info(request, 'Username or Password is Wrong')
    context = {}
    return render(request, 'accounts/home/login.html', context)


def LogoutUser(request):
    logout(request)
    return redirect('home')


@login_required(login_url='login')
def registration(request):
    form = CreateUserForm()
    if request.method =='POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'La cuenta fue Creada '+ user)
            return redirect('login')
    context = {'form':form}
    return render(request, 'accounts/home/registration.html', context)


# @login_required(login_url='login')
def HomeSystem(request):
    countsr = Device.objects.filter(dvt='R').count()
    countsw = Device.objects.filter(dvt='S').count()
    countse = Device.objects.filter(dvt='ED').count()
    countsrw = Device.objects.filter(dvt='RW').count()
    solicitud = Solicitudes.objects.filter(completa=False).all()
    context = {
        'router':countsr,
        'switch':countsw,
        'endev': countse,
        'wifi':countsrw,
        'solicitudes':solicitud

    }
    return render(request, 'accounts/home/homesystem.html', context)


def SendConfiguration(request):
    form = SendConfForm(request.POST or None)
    if form.is_valid():
        obj = form.save()
        obj.user = request.user
        obj.save()
        for device in form.cleaned_data['devices']:
            print(device.dvt)
            conn = paramiko.SSHClient()
            conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            conn.connect(device.ipv4, username=device.username, password=device.clave)
            router_conn = conn.invoke_shell()
            print('Successfully connected to')
            lineas = device.conf_t.splitlines()
            for linea in lineas:
                router_conn.send(linea)
                sleep(1)
                print(router_conn.recv(5000).decode("utf-8"))


    context = {"form": form}
    return render(request, 'accounts/sendconf.html', context)
def Ipv4Ipv6intro(request):
    context = {

    }
    return render(request, 'accounts/ipv4toipv6/intro.html', context)
def Ipv4Ipv6pasos(request):
    context = {

    }
    return render(request, 'accounts/ipv4toipv6/pasos.html', context)

def SegmentacionCalculadoraipv6(request):
    form = SegmentacionForm2(request.POST or None)
    objeto = None
    contar = 0
    if form.is_valid():
        obj = form.save()
        obj.user = request.user
        obj.save()
        objeto = Segmento.objects.last()

        #form = SegmentacionForm()
    context = {
        "form": form,
        "objetos":objeto,
        "contador":contar
    }
    return render(request, 'accounts/ipv4toipv6/segmentacion-calculadora.html', context)

def SegmentacionCalculadora(request):
    form = SegmentacionForm(request.POST or None)
    objeto = None
    if form.is_valid():
        obj = form.save()
        obj.user = request.user
        obj.save()
        objeto = Segmento.objects.last()
    context = {
        "form": form,
        "objetos":objeto,
    }
    return render(request, 'accounts/segmentacion-calculadora.html', context)



def Solicitudcrear(request):
    form = SolicitudForm(request.POST or None)
    if form.is_valid():
        obj = form.save()
        obj.user = request.user
        obj.save()
        form = SolicitudForm()
        redirect('home')
    context = {
        "form": form
    }
    return render(request, 'accounts/solicitud/solicitud.html', context)



def Solicitudver(request, pk):
    obj = get_object_or_404(Solicitudes, pk=pk)
    context = {
        "objeto": obj
    }
    return render(request, 'accounts/solicitud/solicitud-vista.html', context)

def Solicitudf(request, pk):
    obj = get_object_or_404(Solicitudes, pk=pk)
    if obj:
        obj.completa = True
        obj.save()
        redirect('Dashboard')
        return None
    return render(request, 'accounts/solicitud/solicitud-vista.html')

def InventarioListaDevice(request):
    objeto = Device.objects.all()
    context = {
        "objetos":objeto,
    }
    return render(request, 'accounts/device/inventario-lista.html', context)

def InventarioCrear(request):
    form = DeviceForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('Inventario')
    template_name = 'accounts/device/device-crear.html'
    context = {'form': form}
    return render(request, template_name, context)

def InventarioUpdates(request, pk):
    obj = get_object_or_404(Device, pk=pk)
    form = DeviceForm(request.POST or None, instance=obj)
    formset = PuertoFormSet(request.POST or None, instance=obj)
    if form.is_valid() and formset.is_valid():
        formset.save()
        form.save()
        return redirect('Inventario')
    template_name = 'accounts/device/device-edit.html'
    context = {
        "form": form,
        "formset":formset
    }
    return render(request, template_name, context)

def IPListaReverse(request):
    objeto = IpReservada.objects.all()
    context = {
        "objetos":objeto,
    }
    return render(request, 'accounts/ipreservada/lista.html', context)

def IPCrear(request):
    form = IpReservadaForm(request.POST or None)
    if form.is_valid():
        obj = form.save()
        obj.user = request.user
        obj.save()
        return redirect('ip')
    template_name = 'accounts/ipreservada/crear.html'
    context = {'form': form}
    return render(request, template_name, context)

def IPUpdates(request, pk):
    obj = get_object_or_404(IpReservada, pk=pk)
    form = IpReservadaForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('ip')
    template_name = 'accounts/ipreservada/editar.html'
    context = {
        "form": form
    }
    return render(request, template_name, context)


def UbicacionLista(request):
    objeto = Ubicacion.objects.all()
    context = {
        "objetos":objeto,
    }
    return render(request, 'accounts/ubicacion/lista.html', context)

def UbicacionCrear(request):
    form = UbicacionForm(request.POST or None)
    if form.is_valid():
        obj = form.save()
        obj.user = request.user
        obj.save()
        form = UbicacionForm()
        return redirect('Lista Ubicacion')
    template_name = 'accounts/ubicacion/crear.html'
    context = {'form': form}
    return render(request, template_name, context)

def UbicacionUpdate(request, pk):
    obj = get_object_or_404(Ubicacion, pk=pk)
    form = UbicacionForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('Lista Ubicacion')
    template_name = 'accounts/ubicacion/editar.html'
    context = {
        "form": form
    }
    return render(request, template_name, context)