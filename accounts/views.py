from django.shortcuts import render, redirect
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.
def home_view(request):
    context = {}
    return render(request, 'accounts/home.html', context)

def LoginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
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

def HomeSystem(request):
    context = {}
    return render(request, 'accounts/homesystem.html', context)
