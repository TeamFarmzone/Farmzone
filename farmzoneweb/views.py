# Create your views here.
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def forum(request):
    return render(request, 'forum.html')

def profile(request):
    return render(request, 'profile.html')
