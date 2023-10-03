from django.http import FileResponse
from django.shortcuts import render


# Create your views here.
def home(response):
    return render(response, 'home/home.html')


def über(response):
    return render(response, 'home/über.html')


def impressum(response):
    return render(response, 'home/impressum.html')


def view_pdf(response, test_name):
    file_path = f'/herrys_tests_github/herrys_tests/{test_name}.pdf'
    return FileResponse(open(file_path, 'rb'), content_type='application/pdf')
