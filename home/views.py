from django.shortcuts import render, redirect
from home.models import *
from .utils import send_email_to_client

# Create your views here.
def home(request):
    persons = Person.objects.all()
    return render(request, 'home/home.html', context={'peoples': persons, 'page_title': 'Home Page'})

def about(request):
    return render(request, 'home/about.html', context={'page_title': 'About Page'})

def contact(request):
    return render(request, 'home/contact.html', context={'page_title': 'Contact Page'})

def send_email(request):
    send_email_to_client()
    return redirect('/')