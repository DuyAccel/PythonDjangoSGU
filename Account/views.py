
from multiprocessing.dummy import Array
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from Account.models import User
from .forms import MyUserCreationForm


# App Account (Quản lý tài khoản)
def signup (request):
    
    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            login(request, user)
            return redirect('home:home')
        else:
            errors = form.errors
            for error in errors.values():
                messages.error(request, error)
    else:
        form = MyUserCreationForm()
    return render(request, 'sign-up.html', {'form':form})


def signin (request):
    if request.user.is_authenticated:
        return redirect('home:home')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username = username)
        except:
            messages.error(request, 'User is not Exist')  

        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request,user)
            return redirect('home:home')
        else:
            messages.error(request , 'Password is incorect!')
    return render(request, 'sign-in.html')


def signout (request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('home:home')