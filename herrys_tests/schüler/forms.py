from django import forms


class NeuerTest(forms.Form):
    test_name = forms.CharField(label='test_name', widget=forms.HiddenInput(), required=False)
    