from django.shortcuts import render


# Create your views here.
def home(response):
    return render(response, 'home/home.html')


def über(response):
    return render(response, 'home/über.html')


def impressum(response):
    return render(response, 'home/impressum.html')


def datenschutzerklärung(response):
    return render(response, 'home/datenschutzerklärung.html')
