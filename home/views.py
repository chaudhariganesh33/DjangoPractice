from django.shortcuts import render
from home.models import *

# Create your views here.
def home(request):
    persons = Person.objects.all()
    return render(request, 'home/home.html', context={'peoples': persons, 'page_title': 'Home Page'})

def about(request):
    return render(request, 'home/about.html', context={'page_title': 'About Page'})

def contact(request):
    return render(request, 'home/contact.html', context={'page_title': 'Contact Page'})