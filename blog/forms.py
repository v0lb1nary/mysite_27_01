from django import forms
from .models import *
from django.forms import ModelForm

class PostEmailForm(forms.Form):
    """Form definition for PostEmail."""
    nome = forms.CharField(max_length=25)
    email = forms.EmailField()
    para = forms.CharField()
    comentario = forms.CharField(required=False, widget=forms.Textarea)

class ComentariosForm(ModelForm):
    class Meta:
        model = Comentario
        fields = ['nome','email','mensagem',]


