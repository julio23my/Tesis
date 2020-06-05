from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
# Create your views here.
def home_view(request):
    context = {}
    return render(request, 'home.html', context)

def login(request):
    context = {}
    return render(request, 'login.html',context)

def registration(request):
    form = CreateUserForm()
    if request.method =='POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}

    return render(request, 'registration.html',context)