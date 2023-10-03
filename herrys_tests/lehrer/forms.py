from django import forms


# Anzahl der Buchstaben auf 15 minimieren
class NeuerTest(forms.Form):
    test_name = forms.CharField(label='test_name', widget=forms.HiddenInput(), required=False)
    klasse = forms.CharField(label='klasse',
                             widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': "Klasse"}))
    kurs = forms.CharField(label='kurs',
                           widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': "Kurs (z.B. GK)"}))
    lehrer = forms.CharField(label='lehrer',
                             widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': "Lehrkraft"}))
