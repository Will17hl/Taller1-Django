from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    #return HttResponse('<h1>Welcome to Home Page</h1>')
    return render(request, 'home.html', {'name': 'William Andres Henao'})

def about(request):
    return render(request, 'home.html')