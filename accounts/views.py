from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.


def login_page(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        print(username, password)
        if not User.objects.filter(username=username).exists():
            messages.error(request, 'Username does not exist')
            return redirect('/login')
            
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('/recipes')
        else:
            messages.error(request, 'Incorrect Credentials')
            return redirect('/login')
    return render(request, 'accounts/login.html')


def register_page(request):
    if request.method == 'POST':
        data = request.POST

        user = User.objects.filter(username=data.get('username'))
        if user:
            messages.error(request, 'Username already exists')
            return redirect('/register')
        
        user = User.objects.create(
            first_name = data.get('first_name'),
            last_name = data.get('last_name'),
            username = data.get('username')
        )
        user.set_password(data.get('password'))
        user.save()
        messages.success(request, 'User registered successfully')
        return redirect('/register')
    return render(request, 'accounts/register.html')


def logout_page(request):
    logout(request)
    return redirect('/login')