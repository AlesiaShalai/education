__author__ = 'pand0rica'
from django import forms

class DocumentForm(forms.Form):
    docfile = forms.FileField(
        label='Выберите файл',
    )