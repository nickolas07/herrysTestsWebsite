from django.http import FileResponse, HttpResponse
from django.shortcuts import render, redirect
import os
from .models import Test
from .forms import NeuerTest


# Create your views here.
def erstellen(request):
    if request.method == 'POST':
        form = NeuerTest(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            test_name = form.cleaned_data['test_name']
            test_erstellen(test_name)
            return redirect(to=f'pdf/{test_name}')
    else:
        form = NeuerTest()
    return render(request, 'schüler/erstellen.html', {'form': form, 'Tests': Test.objects.all().order_by('name')})


def erstellen_by_jahrgang(request, jahrgang):
    if request.method == 'POST':
        form = NeuerTest(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            test_name = form.cleaned_data['test_name']
            test_erstellen(test_name)
            return redirect(to=f'/pdf/{test_name}')
    else:
        form = NeuerTest()
    return render(request, 'schüler/erstellen.html', {'form': form, 'Tests': Test.objects.all().order_by('name').filter(jahrgang=jahrgang)})


def test_erstellen(test_name):
    test_name = test_name.replace(' ', '_')
    file_path = '/herrys_tests_github/herrys_tests/tests/' + test_name.replace("_-_Lsg", "") + '.py'
    os.system(f'python {file_path}')


def view_pdf(response, test_name):
    file_path = f'/herrys_tests_github/herrys_tests/{test_name}.pdf'
    return FileResponse(open(file_path, 'rb'), content_type='application/pdf')


def download_pdf(response, test_name):
    file_path = f'/herrys_tests_github/herrys_tests/{test_name}.pdf'
    with open(file_path, 'rb') as fh:
        response = HttpResponse(fh.read(), content_type="application/ms-excel")
        response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path).replace('_', ' ')
        return response


def impressum(response):
    return render(response, 'home/impressum.html', {})
