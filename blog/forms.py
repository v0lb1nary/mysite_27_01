from django import forms
from .modlds import *

class PostEmailForm(forms.ModelForm):
    """Form definition for PostEmail."""
    nome = forms.CharField(max_length=30, required=False)
    email = forms.EmailField(required=False)
    para = forms.CharField(max_length=30, required=False)
    comentario = forms.CharField(max_length=250, required=None)
