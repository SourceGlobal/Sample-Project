
from django.shortcuts import render

def home(request):
    return render(request, 'index.html')


def purpose(request):
    return render(request, 'purpose.html')


def contact(request):
    return render(request, 'contact.html')
