from django import forms
from django.forms import ModelForm
from .models import Comentarios

class FormularioPostEmail(forms.Form):
    nome = forms.CharField(max_length=25)
    email = forms.EmailField()
    para = forms.EmailField()
    comentarios = forms.CharField(required=False, widget=forms.Textarea)

class FormularioComentarios(ModelForm):
    class Meta:
        model = Comentarios
        fields = ['nome', 'email', 'mensagem']
