from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    # return HttpResponse("<h1>This is home page</h1>")

    peoples = [
        { 
            'name': 'John',
            'age': 30,
            'city': 'New York'
        },
        { 
            'name': 'Jane',
            'age': 25,
            'city': 'Los Angeles'
        },
        { 
            'name': 'Mike',
            'age': 16,
            'city': 'Chicago'
        },
    ]
    return render(request, 'home/home.html', context={'peoples': peoples, 'page_title': 'Home Page'})

def about(request):
    return render(request, 'home/about.html', context={'page_title': 'About Page'})

def contact(request):
    return render(request, 'home/contact.html', context={'page_title': 'Contact Page'})