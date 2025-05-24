
from django.shortcuts import render

def home(request):
    return render(request, 'index.html')


def purpose(request):
    return render(request, 'purpose.html')


def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')


def objective(request):
    return render(request, 'objective.html')

def background(request):
    return render(request, 'background.html')

