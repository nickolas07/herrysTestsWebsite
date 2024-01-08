from django.http import FileResponse, HttpResponse
from django.shortcuts import render, redirect

import os

from .models import Test
from .forms import NeuerTest

path = '/'.join(os.path.abspath(__file__).split('\\')[:-1])


# Create your views here.
def erstellen(request, jahrgang=None):
    if request.method == 'POST':
        form = NeuerTest(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            test_name = form.cleaned_data['test_name']
            klasse = str(form.cleaned_data['klasse'])
            kurs = form.cleaned_data['kurs'].replace(' ', '_')
            lehrer = form.cleaned_data['lehrer'].replace(' ', '_')
            test_erstellen(test_name=test_name, klasse=klasse, kurs=kurs, lehrer=lehrer)
            return redirect(to=[f'pdf/{test_name}', f'pdf/{test_name} - Lsg'])
    else:
        form = NeuerTest()

    if jahrgang is None:
        return render(request, 'lehrer/erstellen.html',
                      {'form': form, 'Tests': Test.objects.all().order_by('name')})
    else:
        return render(request, 'lehrer/erstellen.html',
                      {'form': form, 'Tests': Test.objects.all().order_by('name').filter(jahrgang=jahrgang)})


def test_erstellen(test_name, klasse, kurs, lehrer):
    test_name = test_name.replace(' ', '_')
    file_path = f'{'/'.join(os.path.abspath(__file__).split('\\')[:-2])}/tests/{test_name.replace("_-_Lsg", "")}.py'
    os.system(f'python {file_path} {klasse} {kurs} {lehrer} lehrer')


def view_pdf(response, test_name):
    if test_name[:8] == 'Vorschau':
        file_path = f'{path}/kontrollen/vorschau/{test_name}.pdf'
    else:
        file_path = f'{path}/kontrollen/erstellt/{test_name}.pdf'

    return FileResponse(open(file_path, 'rb'), content_type='application/pdf')


def download_pdf(response, test_name):
    file_path = f'{path}/kontrollen/erstellt/{test_name}.pdf'
    with open(file_path, 'rb') as fh:
        response = HttpResponse(fh.read(), content_type="application/ms-excel")
        response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path).replace('_', ' ')
        return response
