# Create your views here.
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def forum(request):
    return render(request, 'forum.html')

def marketplace(request):
    return render(request, 'listings.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def contact(request):
    return render(request, 'contact.html')
