from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def home_view(request):
    context = {}
    return render(request, 'home.html', context)

def login(request):
    context = {}
    return render(request, 'login.html',context)

def registration(request):
    form = UserCreationForm()
    if request.method =='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}

    return render(request, 'registration.html',context)