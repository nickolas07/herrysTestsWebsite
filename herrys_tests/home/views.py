from django.shortcuts import render


# Create your views here.
def home(response):
    return render(response, 'home/home.html')


def ueber(response):
    return render(response, 'home/ueber.html')


def impressum(response):
    return render(response, 'home/impressum.html')
