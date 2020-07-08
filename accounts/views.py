from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from .decorators import unauthenticated_user
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import *
# import netmiko
# import napalm


# Create your views here.
def home_view(request):
    context = {}
    return render(request, 'accounts/home.html', context)


@unauthenticated_user
def LoginPage(request):
    if request.method =='POST':
        usernames = request.POST['username']
        passwords = request.POST['password']
        user = authenticate(request, username=usernames, password=passwords)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect('system')
        else:
            messages.info(request, 'Username or Password is Wrong')
    context = {}
    return render(request, 'accounts/login.html',context)


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
    return render(request, 'accounts/registration.html',context)


@login_required(login_url='login')
def HomeSystem(request):
    countsr = Device.objects.filter(dvt='R').count()
    countsw = Device.objects.filter(dvt='SW').count()
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
    return render(request, 'accounts/homesystem.html', context)


@login_required(login_url='login')
def SendConfiguration(request):
    context = {}
    return render(request, 'accounts/sendconf.html', context)


@login_required(login_url='login')
def IPv4toIPv6In(request):
    form = SegmentacionForm(request.POST)
    if form.is_valid():
        obj = form.save()
        obj.user = request.user
        obj.save()
        form = SegmentacionForm()
        print(obj.rango)
    context = {
        "form": form
    }
    return render(request, 'accounts/ipv4toipv6.html', context)

@login_required(login_url='login')
def Solicitudcrear(request):
    form = SolicitudForm(request.POST)
    if form.is_valid():
        obj = form.save()
        obj.user = request.user
        obj.save()
        form = SolicitudForm()
    context = {
        "form": form
    }
    return render(request, 'accounts/solicitud.html', context)


@login_required(login_url='login')
def Solicitudver(request, pk):
    obj = get_object_or_404(Solicitudes, pk=pk)
    context = {
        "objeto": obj
    }
    return render(request, 'accounts/solicitud-vista.html', context)