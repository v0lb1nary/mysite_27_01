from django import forms
from .modlds import *

class PostEmailForm(forms.ModelForm):
    """Form definition for PostEmail."""

    class Meta:
        """Meta definition for PostEmailform."""

        model = PostEmail
        fields = ('',)
